from node import Node, Document, Canvas
from jinja2 import Template
from template import TEMPLATE


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
            return "#FFFFFF"

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


class Rectangle(Vector):
    def __init__(self, node, frame):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()
        self.bg_color = self.color()

    @property
    def corner_radius(self):
        return self.node.get("cornerRadius")

    @property
    def rectangle_corner_radii(self):
        return self.node.get("rectangleCornerRadii")

    def to_code(self):

        return f"""
        ft.Container(
            left={self.x},
            top={self.y},
            width={self.width},
            height={self.height},
            bgcolor="{self.bg_color}",),
"""


class Frame(Node):
    def __init__(self, node):
        super().__init__(node)

        self.width, self.height = self.size()
        self.bg_color = self.color()

        self.counter = {}

        self.elements = [
            self.create_element(child) for child in self.children if Node(child).visible
        ]
        # print(self.elements[0].color)

    def create_element(self, element):
        element_name = element["name"].strip().lower()
        element_type = element["type"].strip().lower()

        # print("Creating Element " f"{{ name: {element_name}, type: {element_type} }}")
        # EXPERIMENTAL FEATURE

        if element_name == "rectangle" or element_type == "rectangle":
            return Rectangle(element, self)
        if element_type == "text":
            return Text(element, self)

    @property
    def children(self):
        # TODO: Convert nodes to Node objects before returning a list of them.
        return self.node.get("children")

    def color(self) -> str:
        """Returns HEX form of element RGB color (str)"""
        try:
            color = self.node["fills"][0]["color"]
            r, g, b, *_ = [int(color.get(i, 0) * 255) for i in "rgba"]
            print("COLOR:", f"#{r:02X}{g:02X}{b:02X}")
            return f"#{r:02X}{g:02X}{b:02X}"

        except Exception:
            return "#FFFFFF"

    def size(self) -> tuple:
        """Returns element dimensions as width (int) and height (int)"""
        bbox = self.node["absoluteBoundingBox"]
        width = bbox["width"]
        height = bbox["height"]
        return int(width), int(height)

    def to_code(self, template):
        t = Template(template)
        rendered_elements = [element.to_code() for element in self.elements if element]
        return t.render(elements=rendered_elements)


class Text(Vector):
    def __init__(self, node, frame):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()

        self.text_color = self.color()
        self.font, self.font_size = self.font_property()
        self.text = self.characters.replace("\n", "\\n")

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
        # TODO: Native conversion
        return self.node.get("style")

    @property
    def style_override_table(self):
        # TODO: Native conversion
        return self.node.get("styleOverrideTable")

    def font_property(self):
        style = self.node.get("style")

        font_name = style.get("fontPostScriptName")
        if font_name is None:
            font_name = style["fontFamily"]

        font_name = font_name.replace("-", " ")
        font_size = style["fontSize"]
        return font_name, font_size

    def to_code(self):
        return f"""
        ft.Container(
            content=ft.Text(value='{self.characters}', size={self.font_size}),
            left={self.x},
            top={self.y},
            width={self.width},
            height={self.height},),
        """


class UnknownElement(Vector):
    def __init__(self, node, frame):
        super().__init__(node)
        self.x, self.y = self.position(frame)
        self.width, self.height = self.size()

    def to_code(self):
        return f"""
ft.Container(
    left{self.x},
    top={self.y},
    width={self.width},
    height{self.height},
    bgcolor="#000000")
"""


test_data = test_data = {
    "id": "1",
    "name": "Frame",
    "type": "FRAME",
    "absoluteBoundingBox": {"x": 10, "y": 20, "width": 300, "height": 200},
    "children": [
        {
            "id": "2",
            "name": "Rectangle 1",
            "type": "RECTANGLE",
            "absoluteBoundingBox": {"x": 15, "y": 25, "width": 150, "height": 50},
            "fills": [{"color": {"r": 1, "g": 0, "b": 0}}],
        },
        {
            "id": "3",
            "name": "Rectangle 2",
            "type": "RECTANGLE",
            "absoluteBoundingBox": {"x": 50, "y": 75, "width": 100, "height": 100},
            "fills": [{"color": {"r": 0, "g": 1, "b": 0}}],
        },
        {
            "id": "1:11",
            "name": "FletEditor",
            "type": "TEXT",
            "scrollBehavior": "SCROLLS",
            "blendMode": "PASS_THROUGH",
            "fills": [
                {
                    "blendMode": "NORMAL",
                    "type": "SOLID",
                    "color": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0},
                }
            ],
            "strokes": [],
            "strokeWeight": 1.0,
            "strokeAlign": "OUTSIDE",
            "absoluteBoundingBox": {
                "x": 1.0,
                "y": -347.0,
                "width": 125.0,
                "height": 29.0,
            },
            "absoluteRenderBounds": {
                "x": 2.992000102996826,
                "y": -342.88800048828125,
                "width": 121.49419403076172,
                "height": 19.079986572265625,
            },
            "constraints": {"vertical": "TOP", "horizontal": "LEFT"},
            "layoutAlign": "INHERIT",
            "layoutGrow": 0.0,
            "layoutSizingHorizontal": "HUG",
            "layoutSizingVertical": "HUG",
            "characters": "FletEditor",
            "style": {
                "fontFamily": "Montserrat",
                "fontPostScriptName": "Montserrat-Bold",
                "fontWeight": 700,
                "textAutoResize": "WIDTH_AND_HEIGHT",
                "fontSize": 24.0,
                "textAlignHorizontal": "LEFT",
                "textAlignVertical": "TOP",
                "letterSpacing": 0.0,
                "lineHeightPx": 29.256000518798828,
                "lineHeightPercent": 100.0,
                "lineHeightUnit": "INTRINSIC_%",
            },
            "layoutVersion": 4,
            "characterStyleOverrides": [],
            "styleOverrideTable": {},
            "lineTypes": ["NONE"],
            "lineIndentations": [0],
            "effects": [],
            "interactions": [],
        },
    ],
}


def main():
    mynode = Node(test_data)
    # document_node = Document(mynode)
    # print(document_node.children)
    # canvas_node = Canvas(document_node.children[0])
    # for n in canvas_node.children:
    frame = Frame(test_data)
    print("\nCODE:", frame.to_code(TEMPLATE))


if __name__ == "__main__":
    main()
