from .node import Node
from .vector_elements import Rectangle, Text, TextField, Image, UnknownElement
from ..utils import download_image
from pathlib import Path


class Frame(Node):
    def __init__(self, node, output_path, figma_file, parent=None):
        super().__init__(node)

        self.parent = parent

        self.width, self.height = self.size()
        self.x, self.y = self.position()
        self.bg_color = self.color()

        self.border_radius = self.get_border_radius()
        self.shadow = self.get_shadow()

        self.counter = {}

        self.figma_file = figma_file

        self.output_path: Path = output_path
        self.assets_path: Path = output_path / "assets"

        self.output_path.mkdir(parents=True, exist_ok=True)
        self.assets_path.mkdir(parents=True, exist_ok=True)

        self.elements = [
            self.create_element(child) for child in self.children if Node(child).visible
        ]

    def create_element(self, element):
        element_name = element["name"].strip().lower()
        element_type = element["type"].strip().lower()

        if element_type == "frame" or element_type == "group":
            return Frame(
                element,
                figma_file=self.figma_file,
                output_path=self.output_path,
                parent=self,
            )
        elif element_name == "textfield":
            return TextField(element, self)

        elif element_type == "rectangle" and element["fills"][0]["type"] == "IMAGE":
            return self.handle_image_element(element)
        if element_name == "rectangle" or element_type == "rectangle":
            return Rectangle(element, self)
        elif element_type == "text":
            return Text(element, self)

        else:
            return UnknownElement(element, self)

    def handle_image_element(self, element):
        self.counter[Image] = self.counter.get(Image, 0) + 1
        item_id = element["id"]
        image_url = self.figma_file.get_image(item_id)
        image_path = self.assets_path / f"image_{self.counter[Image]}.png"
        download_image(image_url, image_path)

        image_path = image_path.relative_to(self.assets_path)

        return Image(element, self, image_path, id_=f"{self.counter[Image]}")

    @property
    def children(self):
        return self.node.get("children")

    def color(self) -> str:
        """Returns HEX form of element RGB color (str)"""
        try:
            color = self.node["fills"][0]["color"]
            r, g, b, *_ = [int(color.get(i, 0) * 255) for i in "rgba"]

            return f"#{r:02X}{g:02X}{b:02X}"

        except Exception:
            return "transparent"

    def size(self) -> tuple:
        """Returns element dimensions as width (int) and height (int)"""
        bbox = self.node["absoluteBoundingBox"]
        width = bbox["width"]
        height = bbox["height"]
        return int(width), int(height)

    def position(self):
        # Returns element coordinates as x (int) and y (int)
        bbox = self.node["absoluteBoundingBox"]
        x = bbox["x"]
        y = bbox["y"]

        #
        if self.parent is None:
            x = 0
            y = 0
        else:
            parent_bbox = self.parent.node["absoluteBoundingBox"]
            x -= parent_bbox["x"]
            y -= parent_bbox["y"]

        return int(x), int(y)

    def get_border_radius(self) -> int:
        if "cornerRadius" in self.node:
            return self.node["cornerRadius"]
        else:
            return 0

    def get_shadow(self) -> dict:
        """Returns the shadow properties as a dictionary."""
        try:
            for effect in self.node.get("effects", []):
                if effect["type"] == "DROP_SHADOW" and effect["visible"]:
                    color = effect["color"]
                    r, g, b, a = [int(color.get(k, 0) * 255) for k in "rgba"]
                    shadow_color = f"#{r:02X}{g:02X}{b:02X}"
                    offset = effect["offset"]
                    blur = effect.get("radius", 0)
                    spread = effect.get("spread", 0)  # Optional
                    return {
                        "color": shadow_color,
                        "offset_x": int(offset["x"]),
                        "offset_y": int(offset["y"]),
                        "blur": int(blur),
                        "spread": int(spread),
                    }
        except KeyError as e:
            print(f"{e}")
        except TypeError as e:
            print(f"TypeError: {e}")
        return None  # No shadow

    def to_code(self):
        # print(self.font_urls)
        # border_radius = self.border_radius
        # border_radius_str = (
        #     f"border_radius=ft.border_radius.all({border_radius[0]})"
        #     if all(r == border_radius[0] for r in border_radius)
        #     else f"border_radius=ft.border_radius.only("
        #     f"topLeft={border_radius[0]}, "
        #     f"topRight={border_radius[1]}, "
        #     f"bottomRight={border_radius[2]}, "
        #     f"bottomLeft={border_radius[3]})"
        # )

        # shadow to Flet-compatible string
        shadow_str = ""
        if self.shadow:
            shadow = self.shadow
            shadow_str = f"""
            shadow=ft.BoxShadow(
                spread_radius={shadow["spread"]},
                blur_radius={shadow["blur"]//5},
                offset=ft.Offset({shadow["offset_x"]}, {shadow["offset_y"]}),
                color="{shadow["color"]}"
            ),
            """

        # Generate code for all child elements
        children_code = ",\n".join(child.to_code() for child in self.elements)
        if children_code:
            return f"""
            ft.Container(
                left={self.x},
                top={self.y},
                width={self.width},
                height={self.height},
                border_radius={self.border_radius},
                {shadow_str}
                bgcolor="{self.bg_color}",
                content=ft.Stack([
                    {children_code},
                ])
            )
        """
        else:
            return f"""
            ft.Container(
                width={self.width},
                height={self.height},
                bgcolor="{self.bg_color}",
            )
            """


class Group(Frame):
    def __init__(self, node):
        super().__init__(node)


class Component(Frame):
    def __init__(self, node):
        super().__init__(node)


class ComponentSet(Frame):
    def __init__(self, node):
        super().__init__(node)
