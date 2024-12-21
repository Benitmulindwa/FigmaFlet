import json
from flet import Page, Container, Text, Row, Column


def process_figma_node(node, parent):
    node_type = node.get("type")
    children = node.get("children", [])
    widget = None

    if node_type == "FRAME":
        widget = Column() if node.get("layoutMode") == "VERTICAL" else Row()
        widget.controls.extend(
            [process_figma_node(child, widget) for child in children]
        )

    elif node_type == "RECTANGLE":
        fills = node.get("fills", [])
        color = fills[0]["color"] if fills else {"r": 1, "g": 1, "b": 1}
        widget = Container(
            bgcolor=f"rgb({int(color['r']*255)}, {int(color['g']*255)}, {int(color['b']*255)})",
            width=node["absoluteBoundingBox"]["width"],
            height=node["absoluteBoundingBox"]["height"],
        )

    elif node_type == "TEXT":
        style = node.get("style", {})
        widget = Text(
            value=node["characters"],
            size=style.get("fontSize", 14),
            weight=style.get("fontWeight", 400),
        )

    if widget and parent:
        parent.controls.append(widget)

    return widget


def generate_flet_app(figma_data):
    figma_structure = json.loads(figma_data)
    root = figma_structure["document"]["children"][0]  # Assuming single page
    page = Page()
    process_figma_node(root, page)
    return page


test_data = """"""

print(generate_flet_app(test_data))
