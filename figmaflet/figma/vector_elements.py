from .node import Node


class Vector(Node):
    def __init__(self, node: dict) -> None:
        super().__init__(node)

    def color(self) -> str:
        """Returns HEX form of element RGB color (str)"""
        try:
            color = self.node["fills"][0]["color"]
            r, g, b, *_ = [int(color.get(i, 0) * 255) for i in "rgba"]

            return f"#{r:02X}{g:02X}{b:02X}"

        except Exception:
            return "transparent"

    def size(self):
        bbox = self.node["absoluteBoundingBox"]
        width = bbox["width"]
        height = bbox["height"]
        return width, height

    def position(self, frame):
        # Returns element coordinates as x (int) and y (int)
        bbox = self.node["absoluteBoundingBox"]
        x = bbox["x"]
        y = bbox["y"]

        frame_bbox = frame.node["absoluteBoundingBox"]
        frame_x = frame_bbox["x"]
        frame_y = frame_bbox["y"]

        x = abs(x - frame_x)
        y = abs(y - frame_y)
        return x, y


# Handled Figma Components
class Rectangle(Vector):
    def __init__(self, node, frame):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()
        self.bg_color = self.color()

    def get_effects(self) -> dict:

        effects = {"shadow": None, "background_blur": None}
        try:
            for effect in self.get("effects", []):
                if effect["type"] == "DROP_SHADOW" and effect["visible"]:
                    shadow_color = self.bg_color
                    offset = effect["offset"]
                    blur = effect.get("radius", 0)
                    spread = effect.get("spread", 0)  # Optional
                    effects["shadow"] = {
                        "color": shadow_color,
                        "offset_x": int(offset["x"]),
                        "offset_y": int(offset["y"]),
                        "blur": int(blur),
                        "spread": int(spread),
                    }
                elif effect["type"] == "BACKGROUND_BLUR" and effect["visible"]:
                    effects["background_blur"] = {"radius": effect.get("radius", 0)}
        except KeyError:
            pass
        return effects

    @property
    def corner_radius(self):
        return self.node.get("cornerRadius")

    @property
    def rectangle_corner_radii(self):
        return self.node.get("rectangleCornerRadii")

    def to_code(self):
        effects = self.get_effects()
        print(effects)
        blur_str = ""
        if effects["background_blur"]:
            blur = effects["background_blur"]
            blur_str = f"blur={blur['radius']},"
        return f"""
        ft.Container(
            left={self.x},
            top={self.y},
            width={self.width},
            height={self.height},
            {blur_str}
            border_radius={self.corner_radius},
            bgcolor="{self.bg_color}",)
"""


class Text(Vector):
    def __init__(self, node, frame):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()

        self.text_color = self.color()
        self.font, self.font_size, self.font_weight = self.font_property()
        if "\n" in self.characters:
            self.text = f'"""{self.characters.replace("\n", "\\n")}"""'
        else:
            self.text = f'"{self.characters}"'

        self.text_align = self.style["textAlignHorizontal"]

    @property
    def characters(self) -> str:
        string: str = self.node.get("characters")
        text_case: str = self.style.get("textCase", "ORIGINAL")

        if text_case == "UPPER":
            string = string.upper()
        elif text_case == "LOWER":
            string = string.lower()
        elif text_case == "TITLE":
            string = string.title()

        return string

    @property
    def style(self):
        return self.node.get("style")

    @property
    def style_override_table(self):
        return self.node.get("styleOverrideTable")

    def font_property(self):
        style = self.node.get("style")

        font_name = style.get("fontPostScriptName")
        if font_name is None:
            font_name = style["fontFamily"]

        # TEXT- Weight
        font_weight = style.get("fontWeight")
        if font_weight:
            font_weight = f"w{font_weight}"

        font_name = font_name.replace("-", " ")
        font_size = style["fontSize"]

        return font_name, font_size, font_weight

    def to_code(self):
        return f"""
        ft.Container(
            content=ft.Text(value={self.text}, size={self.font_size}, color="{self.text_color}",weight="{self.font_weight}",text_align=ft.TextAlign.{self.text_align}),
            left={self.x},
            top={self.y},
            )
        """


class Image(Vector):
    def __init__(self, node, frame, image_path, *, id_):
        super().__init__(node)

        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()

        self.image_path = image_path
        self.id_ = id_

    def to_code(self):
        return f"""
ft.Image(
    src="{self.image_path}",left={self.x},top={self.y},width={self.width},height={self.height})

"""


class UnknownElement(Vector):
    def __init__(self, node, frame):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()

    def to_code(self):
        return f"""
ft.Container(
    left={self.x},
    top={self.y},
    width={self.width},
    height={self.height},
    bgcolor="pink")
"""
