class Node:
    def __init__(self, node: dict):
        self.node = node

    @property
    def id(self) -> str:
        return self.node.get("id")

    @property
    def name(self) -> str:
        return self.node.get("name")

    @property
    def visible(self) -> bool:
        """Whether or not the node is visible on the canvas."""
        return self.node.get("visible", True)

    @property
    def type(self) -> str:
        return self.node.get("type")

    @property
    def plugin_data(self):
        return self.node.get("pluginData")

    @property
    def shared_plugin_data(self):
        return self.node.get("sharedPluginData")

    def get(self, key, default=None):
        return self.node.get(key, default)

    def __repr__(self):
        return f"<Node id={self.id}, name={self.name}, type={self.type}>"


class Document(Node):
    def __init__(self, node, root="window"):
        super().__init__(node)
        self.root = root

    @property
    def children(self) -> list[Node]:
        return [create_node(child) for child in self.node.get("children", [])]


class Canvas(Node):
    def __init__(self, node):
        super().__init__(node)

    @property
    def children(self) -> list[Node]:
        return [create_node(child) for child in self.node.get("children", [])]

    @property
    def background_color(self):
        return self.node.get("backgroundColor")

    @property
    def prototype_start_node_id(self) -> str:
        return self.node.get("prototypeStartNodeID")

    @property
    def export_settings(self):
        return self.node.get("exportSettings")

    def generate(self):
        return ""


class Slice(Node):
    def __init__(self, node):
        super().__init__(node)

    @property
    def export_settings(self):
        return self.node.get("exportSettings")

    @property
    def absolute_bounding_box(self):
        return self.node.get("absoluteBoundingBox")

    @property
    def size(self):
        return self.node.get("size")

    @property
    def relative_transform(self):
        return self.node.get("relativeTransform")


# Factory Method
def create_node(node_data: dict) -> Node:
    node_type = node_data.get("type")
    if node_type == "DOCUMENT":
        return Document(node_data)
    elif node_type == "CANVAS":
        return Canvas(node_data)
    elif node_type == "SLICE":
        return Slice(node_data)
    # Add other node types here as needed
    return Node(node_data)
