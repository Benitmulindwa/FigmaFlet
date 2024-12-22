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


test_data = {
    "id": "1",
    "name": "Frame",
    "type": "FRAME",
    "absoluteBoundingBox": {"x": 10, "y": 20, "width": 200, "height": 100},
    "children": [
        {
            "id": "2",
            "name": "Rectangle 1",
            "type": "RECTANGLE",
            "absoluteBoundingBox": {"x": 15, "y": 25, "width": 150, "height": 50},
            "fills": [{"color": {"r": 1, "g": 0, "b": 0}}],
        }
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


class Text(Node):
    def __init__(self, node):
        super().__init__(node)

    @property
    def content(self):
        return self.node.get("characters", "")

    @property
    def font_size(self):
        return self.node.get("style", {}).get("fontSize", 14)

    def to_code(self):
        return f"ft.Text(value='{self.content}', size={self.font_size})"


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
