from .node import Node


class Vector(Node):
    def __init__(self, node: dict) -> None:
        super().__init__(node)

    def strockes_color(self):
        try:
            strokes = self.node.get("strokes", [])
            if strokes:
                stroke = strokes[0]
                color = stroke.get("color", {})
                r, g, b, *_ = [int(color.get(i, 0) * 255) for i in "rgba"]
                # Extract opacity (default to 1 if not provided)
                opacity = stroke.get("opacity", 1) * self.node.get("opacity", 1)
                return [round(opacity, 2), f"#{r:02X}{g:02X}{b:02X}"]
        except:
            return [1, "transparent"]

    def color(self) -> str:
        """Returns HEX form of element RGB color (str)"""
        fills = self.node.get("fills", [])
        if fills:
            try:
                fill = fills[0]
                color = fill.get("color", {})
                r, g, b, *_ = [int(color.get(i, 0) * 255) for i in "rgba"]
                # Extract opacity (default to 1 if not provided)
                opacity = fill.get("opacity", 1) * self.node.get("opacity", 1)

                return [round(opacity, 2), f"#{r:02X}{g:02X}{b:02X}"]

            except Exception:
                return [1, "transparent"]

    def size(self):
        bbox = self.node.get("absoluteBoundingBox", {})
        width = bbox.get("width", 0)
        height = bbox.get("height", 0)
        return int(width), int(height)

    def position(self, frame):
        # Returns element coordinates as x (int) and y (int)
        bbox = self.node.get("absoluteBoundingBox", {})
        x = bbox["x"]
        y = bbox["y"]

        frame_bbox = frame.node.get("absoluteBoundingBox")
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
        self.opacity, self.bg_color = self.color()
        self.gradient = None
        self.border_str = ""
        self.border_width = int(self.node.get("strokeWeight", 2.0))
        if self.strockes_color():
            self.border_opacity, self.border_color = self.strockes_color()
            self.border_str = f"border=ft.border.all({self.border_width},ft.Colors.with_opacity({self.border_opacity},'{self.border_color}')),"

    def get_effects(self) -> dict:

        effects = {"shadow": None, "background_blur": None, "gradient": None}
        try:
            for effect in self.get("effects", []):
                if effect["type"] == "DROP_SHADOW" and effect["visible"]:
                    color = effect.get("color", {})
                    r, g, b, *_ = [int(color.get(i, 0) * 255) for i in "rgba"]
                    shadow_color = f"#{r:02X}{g:02X}{b:02X}"

                    offset = effect.get("offset", {"x": 0, "y": 0})
                    blur = effect.get("radius", 0)

                    effects["shadow"] = {
                        "color": shadow_color,
                        "offset_x": int(offset["x"]) / 2,
                        "offset_y": int(offset["y"]) / 2,
                        "blur": int(blur),
                    }
                elif effect["type"] == "BACKGROUND_BLUR" and effect["visible"]:
                    effects["background_blur"] = {"radius": effect.get("radius", 0)}
            for fill in self.get("fills", []):
                gradient_stops = fill.get("gradientStops", [])
                hex_colors = [
                    f"""ft.Colors.with_opacity({round(color['a'],3)}, "#{int(color['r'] * 255):02x}{int(color['g'] * 255):02x}{int(color['b'] * 255):02x}")"""
                    for stop in gradient_stops
                    for color in [stop["color"]]
                ]
                if fill["type"] == "GRADIENT_LINEAR":

                    gradient_pos = fill.get("gradientHandlePositions", [])

                    begin_pos = gradient_pos[0]
                    end_pos = gradient_pos[1]

                    # Map to Flet's Alignment (x, y)
                    begin = f"ft.Alignment({round(end_pos['x'],2)}, {round(end_pos['y'],2)})"
                    end = f"ft.Alignment({round(begin_pos['x'],2)}, {round(begin_pos['y'],2)})"
                    # print(begin, end)

                    if len(gradient_stops) < 2:
                        raise ValueError("Gradient must have at least two stops.")

                    effects["gradient"] = {
                        "type": fill["type"],
                        "colors": hex_colors,
                        "stops": [stop["position"] for stop in gradient_stops],
                        "begin": begin,
                        "end": end,
                    }
                elif fill["type"] == "GRADIENT_RADIAL":
                    gradient_center = fill.get("gradientHandlePositions", [])
                    if len(gradient_center) < 3:
                        raise ValueError(
                            "Radial gradient must have valid handle positions (center and radii)."
                        )

                    # The center position is the first handle
                    center = gradient_center[0]
                    radius_start = gradient_center[1]
                    radius_end = gradient_center[2]

                    # Map to Flet's Alignment (x, y)
                    center_alignment = f"ft.Alignment({round(center['x'], 2)}, {round(center['y'], 2)})"
                    radius = round(
                        (
                            (radius_end["x"] - radius_start["x"]) ** 2
                            + (radius_end["y"] - radius_start["y"]) ** 2
                        )
                        ** 0.5,
                        2,
                    )

                    effects["gradient"] = {
                        "type": fill["type"],
                        "colors": hex_colors,
                        "stops": [stop["position"] for stop in gradient_stops],
                        "center": center_alignment,
                        "radius": radius,
                    }

        except KeyError as e:
            print(f"Missing key in effect data: {e}")
        except TypeError as e:
            print(f"Unexpected NoneType: {e}")
        return effects

    @property
    def corner_radius(self):
        return self.node.get("cornerRadius")

    @property
    def rectangle_corner_radii(self):
        return self.node.get("rectangleCornerRadii")

    def to_code(self):
        effects = self.get_effects()
        gradient_str = ""
        if effects["gradient"]:
            gradient = effects["gradient"]
            if gradient["type"] == "GRADIENT_LINEAR":
                gradient_str = f"""
                gradient=ft.LinearGradient(
                    colors=[{", ".join(gradient['colors'])}],
                    # stops={gradient['stops']},
                    begin={gradient['begin']},
                    end={gradient['end']},
                    rotation=3.1415
                )
                """
            if gradient["type"] == "GRADIENT_RADIAL":
                gradient_str = f"""
                gradient=ft.RadialGradient(
                    colors=[{", ".join(gradient['colors'])}],
                    stops={gradient['stops']},
                )
                """

        # Shadow to flet compatible str
        shadow_str = ""
        if effects["shadow"]:
            shadow = effects["shadow"]
            shadow_str = f"""
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius={shadow['blur']//5},
                offset=ft.Offset({shadow['offset_x']}, {shadow['offset_y']}),
                color=ft.Colors.with_opacity(0.1,"{shadow['color']}")
            ),
            """
        # blur to flet compatible str
        blur_str = ""
        if effects["background_blur"]:
            blur = effects["background_blur"]
            blur_str = f"blur={blur['radius']//2},"

        return f"""
        ft.Container(
            left={self.x},
            top={self.y},
            width={self.width},
            height={self.height},
            {blur_str}
            {shadow_str}
            border_radius={self.corner_radius},
            {self.border_str}
            bgcolor=ft.Colors.with_opacity({self.opacity},'{self.bg_color}'),
            {gradient_str}
            )
"""


class Text(Vector):
    def __init__(self, node, frame):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()

        self.text_opacity, self.text_color = self.color()

        self.font_family, self.font_size, self.font_weight = self.font_property()

        if "\n" in self.characters:
            self.text = f'"""{self.characters.replace("\n", "\\n")}"""'
        else:
            self.text = f"'{self.characters}'"

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
            content=ft.Text(value={self.text}, size={self.font_size}, color='{self.text_color}',weight='{self.font_weight}',font_family="{self.font_family}",text_align=ft.TextAlign.{self.text_align}),
            left={self.x},
            top={self.y},
            )
        """


class TextField(Vector):
    def __init__(self, node, frame, hint_text, label_text, is_password):
        super().__init__(node)

        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()
        self.border_opacity, self.border_color = self.strockes_color()
        self.border_width = int(self.node.get("strokeWeight", 2.0))
        self.opacity, self.bg_color = self.color()

        self.border_radius = self.get("cornerRadius", 0)

        self.hint_text = hint_text
        self.label_text = label_text

        self.is_password = is_password

    def text_color_from_bg(self, bg_color):
        # Assuming bg_color is a hex string like "#RRGGBB"
        bg_color = bg_color.lstrip("#")

        # hex to RGB
        r, g, b = int(bg_color[0:2], 16), int(bg_color[2:4], 16), int(bg_color[4:6], 16)

        # luminance
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255

        # Choose text color based on luminance
        return "#FFFFFF" if luminance < 0.5 else "#000000"

    def to_code(self):
        password_str = ""
        info_str = ""
        if self.hint_text != "":
            info_str = f"hint_text='{self.hint_text}',"

        elif self.label_text != "":
            info_str = f"label='{self.label_text}',"

        if self.is_password:
            password_str = f"""
                can_reveal_password={self.is_password},
                password={self.is_password}"""
        content_pad = int(self.height - (self.height / 1.5)) / 2

        return f"""
        ft.Container(
            content=ft.TextField(
                width={self.width},
                height={self.height},
                border_color=ft.Colors.with_opacity({self.border_opacity},'{self.border_color}'),
                border_radius={self.border_radius},
                bgcolor=ft.Colors.with_opacity({self.opacity},'{self.bg_color}'),
                cursor_height={self.height/1.5},
                cursor_color='{self.text_color_from_bg(self.bg_color)}',
                focused_border_color='{self.border_color}',
                content_padding={content_pad},
                text_style=ft.TextStyle(color="{self.text_color_from_bg(self.bg_color)}"),
                {info_str}
                {password_str}
                ),
            left={self.x},
            top={self.y}, )
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


class Button(Vector):
    def __init__(self, node, frame, text="", text_color="#ffffff"):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()

        self.text = text
        self.text_color = text_color

    def to_flet(self):
        # Extract background color and corner radius
        opacity, bg_color = self.color()
        radius = self.node.get("cornerRadius", 5)

        # Generate Flet button code
        return f"""
        ft.FilledButton(
            text='{self.text}',
            width={self.width},
            hight={self.height},
            style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius={radius}),
            bgcolor={{
                    ft.ControlState.DEFAULT: '{bg_color}',
                    ft.ControlState.HOVERED: '',
                }},
            color='{self.text_color}'
            ),
            left={self.x},
            top={self.y},
        )"""


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
