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
            bgcolor="{self.bg_color}",)
"""


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
            height={self.height},)
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
        if element_type == "frame":
            return Frame(element)
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

            return f"#{r:02X}{g:02X}{b:02X}"

        except Exception:
            return "#FFFFFF"

    def size(self) -> tuple:
        """Returns element dimensions as width (int) and height (int)"""
        bbox = self.node["absoluteBoundingBox"]
        width = bbox["width"]
        height = bbox["height"]
        return int(width), int(height)

    def to_code(self, template=None):
        # Generate code for all child elements
        children_code = ",\n".join(child.to_code() for child in self.elements)
        if children_code:
            return f"""
            ft.Container(
                width={self.width},
                height={self.height},
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

    # def to_code(self, template):
    #     t = Template(template)
    #     # Flatten the hierarchy of elements
    #     all_elements = self.flatten_elements()
    #     return t.render(elements=all_elements)

    # def flatten_elements(self):
    #     """Recursively collect all child elements."""
    #     all_elements = []
    #     for element in self.elements:
    #         if isinstance(element, Frame):
    #             all_elements.extend(element.flatten_elements())
    #         elif element:
    #             all_elements.append(element)
    #     return all_elements


test_data = {
    "id": "1",
    "name": "Main Frame",
    "type": "FRAME",
    "absoluteBoundingBox": {"x": 0, "y": 0, "width": 600, "height": 400},
    "children": [
        {
            "id": "2",
            "name": "Rectangle 1",
            "type": "RECTANGLE",
            "absoluteBoundingBox": {"x": 10, "y": 20, "width": 200, "height": 100},
            "fills": [{"color": {"r": 1, "g": 0, "b": 0}}],
        },
        {
            "id": "3",
            "name": "Nested Frame",
            "type": "FRAME",
            "absoluteBoundingBox": {"x": 50, "y": 60, "width": 300, "height": 200},
            "children": [
                {
                    "id": "4",
                    "name": "Text in Nested Frame",
                    "type": "TEXT",
                    "absoluteBoundingBox": {
                        "x": 60,
                        "y": 80,
                        "width": 100,
                        "height": 30,
                    },
                    "characters": "Nested Text",
                    "style": {
                        "fontFamily": "Montserrat",
                        "fontPostScriptName": "Montserrat-Regular",
                        "fontWeight": 400,
                        "textAutoResize": "WIDTH_AND_HEIGHT",
                        "fontSize": 15.0,
                        "textAlignHorizontal": "CENTER",
                        "textAlignVertical": "TOP",
                        "letterSpacing": 0.0,
                        "lineHeightPx": 21.941999435424805,
                        "lineHeightPercent": 100.0,
                        "lineHeightUnit": "INTRINSIC_%",
                    },
                    "fills": [{"color": {"r": 0, "g": 0, "b": 1}}],
                }
            ],
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
