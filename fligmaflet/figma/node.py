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


class Document(Node):
    def __init__(self, node, root="window"):
        super().__init__(node)
        self.root = root

    @property
    def children(self) -> list[dict]:
        return self.node.get("children")


class Canvas(Node):
    def __init__(self, node):
        super().__init__(node)

    @property
    def children(self):
        # TODO: Convert nodes to Node objects before returning a list of them.
        return self.node.get("children")

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


test_data = {
    "document": {
        "id": "0:0",
        "name": "Document",
        "type": "DOCUMENT",
        "scrollBehavior": "SCROLLS",
        "children": [
            {
                "id": "0:1",
                "name": "Page 1",
                "type": "CANVAS",
                "scrollBehavior": "SCROLLS",
                "children": [
                    {
                        "id": "1:2",
                        "name": "Main",
                        "type": "FRAME",
                        "scrollBehavior": "SCROLLS",
                        "children": [
                            {
                                "id": "1:3",
                                "name": "Rectangle 1",
                                "type": "RECTANGLE",
                                "locked": True,
                                "scrollBehavior": "SCROLLS",
                                "blendMode": "PASS_THROUGH",
                                "fills": [
                                    {
                                        "blendMode": "NORMAL",
                                        "type": "SOLID",
                                        "color": {
                                            "r": 0.0,
                                            "g": 0.0,
                                            "b": 0.0,
                                            "a": 1.0,
                                        },
                                    }
                                ],
                                "strokes": [],
                                "strokeWeight": 1.0,
                                "strokeAlign": "INSIDE",
                                "absoluteBoundingBox": {
                                    "x": -79.0,
                                    "y": -384.0,
                                    "width": 1440.0,
                                    "height": 900.0,
                                },
                                "absoluteRenderBounds": {
                                    "x": -79.0,
                                    "y": -384.0,
                                    "width": 1440.0,
                                    "height": 900.0,
                                },
                                "constraints": {
                                    "vertical": "TOP",
                                    "horizontal": "LEFT",
                                },
                                "effects": [],
                                "interactions": [],
                            },
                            {
                                "id": "1:76",
                                "name": "Main Menu",
                                "type": "FRAME",
                                "locked": True,
                                "scrollBehavior": "SCROLLS",
                                "children": [
                                    {
                                        "id": "1:75",
                                        "name": "Frame 2",
                                        "type": "FRAME",
                                        "scrollBehavior": "SCROLLS",
                                        "children": [
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
                                                        "color": {
                                                            "r": 1.0,
                                                            "g": 1.0,
                                                            "b": 1.0,
                                                            "a": 1.0,
                                                        },
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
                                                "constraints": {
                                                    "vertical": "TOP",
                                                    "horizontal": "LEFT",
                                                },
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
                                            {
                                                "id": "1:10",
                                                "name": "Frame 1",
                                                "type": "FRAME",
                                                "scrollBehavior": "SCROLLS",
                                                "children": [
                                                    {
                                                        "id": "1:4",
                                                        "name": "Main",
                                                        "type": "TEXT",
                                                        "scrollBehavior": "SCROLLS",
                                                        "blendMode": "PASS_THROUGH",
                                                        "fills": [
                                                            {
                                                                "blendMode": "NORMAL",
                                                                "type": "SOLID",
                                                                "color": {
                                                                    "r": 1.0,
                                                                    "g": 1.0,
                                                                    "b": 1.0,
                                                                    "a": 1.0,
                                                                },
                                                            }
                                                        ],
                                                        "strokes": [],
                                                        "strokeWeight": 1.0,
                                                        "strokeAlign": "OUTSIDE",
                                                        "absoluteBoundingBox": {
                                                            "x": 409.0,
                                                            "y": -343.5,
                                                            "width": 46.0,
                                                            "height": 22.0,
                                                        },
                                                        "absoluteRenderBounds": {
                                                            "x": 410.8900146484375,
                                                            "y": -340.1260070800781,
                                                            "width": 41.778564453125,
                                                            "height": 13.7340087890625,
                                                        },
                                                        "constraints": {
                                                            "vertical": "TOP",
                                                            "horizontal": "LEFT",
                                                        },
                                                        "layoutAlign": "INHERIT",
                                                        "layoutGrow": 0.0,
                                                        "layoutSizingHorizontal": "HUG",
                                                        "layoutSizingVertical": "HUG",
                                                        "characters": "Main",
                                                        "style": {
                                                            "fontFamily": "Montserrat",
                                                            "fontPostScriptName": "Montserrat-Medium",
                                                            "fontWeight": 500,
                                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                                            "fontSize": 18.0,
                                                            "textAlignHorizontal": "LEFT",
                                                            "textAlignVertical": "TOP",
                                                            "letterSpacing": 0.0,
                                                            "lineHeightPx": 21.941999435424805,
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
                                                    {
                                                        "id": "1:5",
                                                        "name": "About",
                                                        "type": "TEXT",
                                                        "scrollBehavior": "SCROLLS",
                                                        "blendMode": "PASS_THROUGH",
                                                        "fills": [
                                                            {
                                                                "blendMode": "NORMAL",
                                                                "type": "SOLID",
                                                                "color": {
                                                                    "r": 1.0,
                                                                    "g": 1.0,
                                                                    "b": 1.0,
                                                                    "a": 1.0,
                                                                },
                                                            }
                                                        ],
                                                        "strokes": [],
                                                        "strokeWeight": 1.0,
                                                        "strokeAlign": "OUTSIDE",
                                                        "absoluteBoundingBox": {
                                                            "x": 495.0,
                                                            "y": -343.5,
                                                            "width": 57.0,
                                                            "height": 22.0,
                                                        },
                                                        "absoluteRenderBounds": {
                                                            "x": 494.98199462890625,
                                                            "y": -339.8559875488281,
                                                            "width": 56.08056640625,
                                                            "height": 13.4639892578125,
                                                        },
                                                        "constraints": {
                                                            "vertical": "TOP",
                                                            "horizontal": "LEFT",
                                                        },
                                                        "layoutAlign": "INHERIT",
                                                        "layoutGrow": 0.0,
                                                        "layoutSizingHorizontal": "HUG",
                                                        "layoutSizingVertical": "HUG",
                                                        "characters": "About",
                                                        "style": {
                                                            "fontFamily": "Montserrat",
                                                            "fontPostScriptName": "Montserrat-Medium",
                                                            "fontWeight": 500,
                                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                                            "fontSize": 18.0,
                                                            "textAlignHorizontal": "LEFT",
                                                            "textAlignVertical": "TOP",
                                                            "letterSpacing": 0.0,
                                                            "lineHeightPx": 21.941999435424805,
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
                                                    {
                                                        "id": "1:6",
                                                        "name": "Program",
                                                        "type": "TEXT",
                                                        "scrollBehavior": "SCROLLS",
                                                        "blendMode": "PASS_THROUGH",
                                                        "fills": [
                                                            {
                                                                "blendMode": "NORMAL",
                                                                "type": "SOLID",
                                                                "color": {
                                                                    "r": 1.0,
                                                                    "g": 1.0,
                                                                    "b": 1.0,
                                                                    "a": 1.0,
                                                                },
                                                            }
                                                        ],
                                                        "strokes": [],
                                                        "strokeWeight": 1.0,
                                                        "strokeAlign": "OUTSIDE",
                                                        "absoluteBoundingBox": {
                                                            "x": 592.0,
                                                            "y": -343.5,
                                                            "width": 80.0,
                                                            "height": 22.0,
                                                        },
                                                        "absoluteRenderBounds": {
                                                            "x": 593.8900146484375,
                                                            "y": -339.1000061035156,
                                                            "width": 76.5665283203125,
                                                            "height": 16.20001220703125,
                                                        },
                                                        "constraints": {
                                                            "vertical": "TOP",
                                                            "horizontal": "LEFT",
                                                        },
                                                        "layoutAlign": "INHERIT",
                                                        "layoutGrow": 0.0,
                                                        "layoutSizingHorizontal": "HUG",
                                                        "layoutSizingVertical": "HUG",
                                                        "characters": "Program",
                                                        "style": {
                                                            "fontFamily": "Montserrat",
                                                            "fontPostScriptName": "Montserrat-Medium",
                                                            "fontWeight": 500,
                                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                                            "fontSize": 18.0,
                                                            "textAlignHorizontal": "LEFT",
                                                            "textAlignVertical": "TOP",
                                                            "letterSpacing": 0.0,
                                                            "lineHeightPx": 21.941999435424805,
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
                                                    {
                                                        "id": "1:9",
                                                        "name": "Price",
                                                        "type": "TEXT",
                                                        "scrollBehavior": "SCROLLS",
                                                        "blendMode": "PASS_THROUGH",
                                                        "fills": [
                                                            {
                                                                "blendMode": "NORMAL",
                                                                "type": "SOLID",
                                                                "color": {
                                                                    "r": 1.0,
                                                                    "g": 1.0,
                                                                    "b": 1.0,
                                                                    "a": 1.0,
                                                                },
                                                            }
                                                        ],
                                                        "strokes": [],
                                                        "strokeWeight": 1.0,
                                                        "strokeAlign": "OUTSIDE",
                                                        "absoluteBoundingBox": {
                                                            "x": 712.0,
                                                            "y": -343.5,
                                                            "width": 47.0,
                                                            "height": 22.0,
                                                        },
                                                        "absoluteRenderBounds": {
                                                            "x": 713.8900146484375,
                                                            "y": -340.1260070800781,
                                                            "width": 43.4383544921875,
                                                            "height": 13.7340087890625,
                                                        },
                                                        "constraints": {
                                                            "vertical": "TOP",
                                                            "horizontal": "LEFT",
                                                        },
                                                        "layoutAlign": "INHERIT",
                                                        "layoutGrow": 0.0,
                                                        "layoutSizingHorizontal": "HUG",
                                                        "layoutSizingVertical": "HUG",
                                                        "characters": "Price",
                                                        "style": {
                                                            "fontFamily": "Montserrat",
                                                            "fontPostScriptName": "Montserrat-Medium",
                                                            "fontWeight": 500,
                                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                                            "fontSize": 18.0,
                                                            "textAlignHorizontal": "LEFT",
                                                            "textAlignVertical": "TOP",
                                                            "letterSpacing": 0.0,
                                                            "lineHeightPx": 21.941999435424805,
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
                                                    {
                                                        "id": "1:7",
                                                        "name": "Contact",
                                                        "type": "TEXT",
                                                        "scrollBehavior": "SCROLLS",
                                                        "blendMode": "PASS_THROUGH",
                                                        "fills": [
                                                            {
                                                                "blendMode": "NORMAL",
                                                                "type": "SOLID",
                                                                "color": {
                                                                    "r": 1.0,
                                                                    "g": 1.0,
                                                                    "b": 1.0,
                                                                    "a": 1.0,
                                                                },
                                                            }
                                                        ],
                                                        "strokes": [],
                                                        "strokeWeight": 1.0,
                                                        "strokeAlign": "OUTSIDE",
                                                        "absoluteBoundingBox": {
                                                            "x": 799.0,
                                                            "y": -343.5,
                                                            "width": 73.0,
                                                            "height": 22.0,
                                                        },
                                                        "absoluteRenderBounds": {
                                                            "x": 799.864013671875,
                                                            "y": -339.2439880371094,
                                                            "width": 71.03643798828125,
                                                            "height": 12.88800048828125,
                                                        },
                                                        "constraints": {
                                                            "vertical": "TOP",
                                                            "horizontal": "LEFT",
                                                        },
                                                        "layoutAlign": "INHERIT",
                                                        "layoutGrow": 0.0,
                                                        "layoutSizingHorizontal": "HUG",
                                                        "layoutSizingVertical": "HUG",
                                                        "characters": "Contact",
                                                        "style": {
                                                            "fontFamily": "Montserrat",
                                                            "fontPostScriptName": "Montserrat-Medium",
                                                            "fontWeight": 500,
                                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                                            "fontSize": 18.0,
                                                            "textAlignHorizontal": "LEFT",
                                                            "textAlignVertical": "TOP",
                                                            "letterSpacing": 0.0,
                                                            "lineHeightPx": 21.941999435424805,
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
                                                "blendMode": "PASS_THROUGH",
                                                "clipsContent": False,
                                                "background": [],
                                                "fills": [],
                                                "strokes": [],
                                                "strokeWeight": 1.0,
                                                "strokeAlign": "INSIDE",
                                                "backgroundColor": {
                                                    "r": 0.0,
                                                    "g": 0.0,
                                                    "b": 0.0,
                                                    "a": 0.0,
                                                },
                                                "layoutMode": "HORIZONTAL",
                                                "itemSpacing": 40.0,
                                                "counterAxisAlignItems": "CENTER",
                                                "layoutWrap": "NO_WRAP",
                                                "absoluteBoundingBox": {
                                                    "x": 409.0,
                                                    "y": -343.5,
                                                    "width": 463.0,
                                                    "height": 22.0,
                                                },
                                                "absoluteRenderBounds": {
                                                    "x": 409.0,
                                                    "y": -343.5,
                                                    "width": 463.0,
                                                    "height": 22.0,
                                                },
                                                "constraints": {
                                                    "vertical": "TOP",
                                                    "horizontal": "LEFT",
                                                },
                                                "layoutAlign": "INHERIT",
                                                "layoutGrow": 0.0,
                                                "layoutSizingHorizontal": "HUG",
                                                "layoutSizingVertical": "HUG",
                                                "effects": [],
                                                "interactions": [],
                                            },
                                            {
                                                "id": "1:73",
                                                "name": "bxl:instagram-alt",
                                                "type": "FRAME",
                                                "scrollBehavior": "SCROLLS",
                                                "children": [
                                                    {
                                                        "id": "1:15",
                                                        "name": "Vector",
                                                        "type": "VECTOR",
                                                        "scrollBehavior": "SCROLLS",
                                                        "blendMode": "PASS_THROUGH",
                                                        "fills": [
                                                            {
                                                                "blendMode": "NORMAL",
                                                                "type": "SOLID",
                                                                "color": {
                                                                    "r": 1.0,
                                                                    "g": 1.0,
                                                                    "b": 1.0,
                                                                    "a": 1.0,
                                                                },
                                                            }
                                                        ],
                                                        "strokes": [],
                                                        "strokeWeight": 1.0,
                                                        "strokeAlign": "INSIDE",
                                                        "absoluteBoundingBox": {
                                                            "x": 1155.0,
                                                            "y": -342.5,
                                                            "width": 20.0,
                                                            "height": 20.0,
                                                        },
                                                        "absoluteRenderBounds": {
                                                            "x": 1155.0,
                                                            "y": -342.5,
                                                            "width": 20.0,
                                                            "height": 20.0,
                                                        },
                                                        "constraints": {
                                                            "vertical": "TOP",
                                                            "horizontal": "LEFT",
                                                        },
                                                        "layoutAlign": "INHERIT",
                                                        "layoutGrow": 0.0,
                                                        "layoutSizingHorizontal": "FIXED",
                                                        "layoutSizingVertical": "FIXED",
                                                        "effects": [],
                                                        "interactions": [],
                                                    },
                                                    {
                                                        "id": "1:17",
                                                        "name": "Vector",
                                                        "type": "VECTOR",
                                                        "scrollBehavior": "SCROLLS",
                                                        "blendMode": "PASS_THROUGH",
                                                        "fills": [
                                                            {
                                                                "blendMode": "NORMAL",
                                                                "type": "SOLID",
                                                                "color": {
                                                                    "r": 1.0,
                                                                    "g": 1.0,
                                                                    "b": 1.0,
                                                                    "a": 1.0,
                                                                },
                                                            }
                                                        ],
                                                        "strokes": [],
                                                        "strokeWeight": 1.0,
                                                        "strokeAlign": "INSIDE",
                                                        "absoluteBoundingBox": {
                                                            "x": 1185.0,
                                                            "y": -341.5,
                                                            "width": 18.0,
                                                            "height": 18.0,
                                                        },
                                                        "absoluteRenderBounds": {
                                                            "x": 1185.0,
                                                            "y": -341.5,
                                                            "width": 18.0,
                                                            "height": 18.0,
                                                        },
                                                        "constraints": {
                                                            "vertical": "TOP",
                                                            "horizontal": "LEFT",
                                                        },
                                                        "layoutAlign": "INHERIT",
                                                        "layoutGrow": 0.0,
                                                        "layoutSizingHorizontal": "FIXED",
                                                        "layoutSizingVertical": "FIXED",
                                                        "effects": [],
                                                        "interactions": [],
                                                    },
                                                ],
                                                "blendMode": "PASS_THROUGH",
                                                "clipsContent": False,
                                                "background": [],
                                                "fills": [],
                                                "strokes": [],
                                                "strokeWeight": 1.0,
                                                "strokeAlign": "INSIDE",
                                                "backgroundColor": {
                                                    "r": 0.0,
                                                    "g": 0.0,
                                                    "b": 0.0,
                                                    "a": 0.0,
                                                },
                                                "layoutMode": "HORIZONTAL",
                                                "itemSpacing": 10.0,
                                                "primaryAxisSizingMode": "FIXED",
                                                "counterAxisAlignItems": "CENTER",
                                                "layoutWrap": "NO_WRAP",
                                                "absoluteBoundingBox": {
                                                    "x": 1155.0,
                                                    "y": -342.5,
                                                    "width": 68.0,
                                                    "height": 20.0,
                                                },
                                                "absoluteRenderBounds": {
                                                    "x": 1155.0,
                                                    "y": -342.5,
                                                    "width": 68.0,
                                                    "height": 20.0,
                                                },
                                                "constraints": {
                                                    "vertical": "TOP",
                                                    "horizontal": "LEFT",
                                                },
                                                "layoutAlign": "INHERIT",
                                                "layoutGrow": 0.0,
                                                "layoutSizingHorizontal": "FIXED",
                                                "layoutSizingVertical": "HUG",
                                                "effects": [],
                                                "interactions": [],
                                            },
                                        ],
                                        "blendMode": "PASS_THROUGH",
                                        "clipsContent": False,
                                        "background": [],
                                        "fills": [],
                                        "strokes": [],
                                        "strokeWeight": 1.0,
                                        "strokeAlign": "INSIDE",
                                        "backgroundColor": {
                                            "r": 0.0,
                                            "g": 0.0,
                                            "b": 0.0,
                                            "a": 0.0,
                                        },
                                        "layoutMode": "HORIZONTAL",
                                        "itemSpacing": 283.0,
                                        "counterAxisAlignItems": "CENTER",
                                        "layoutWrap": "NO_WRAP",
                                        "absoluteBoundingBox": {
                                            "x": 1.0,
                                            "y": -347.0,
                                            "width": 1222.0,
                                            "height": 29.0,
                                        },
                                        "absoluteRenderBounds": {
                                            "x": 1.0,
                                            "y": -347.0,
                                            "width": 1222.0,
                                            "height": 29.0,
                                        },
                                        "constraints": {
                                            "vertical": "TOP",
                                            "horizontal": "LEFT",
                                        },
                                        "layoutSizingHorizontal": "HUG",
                                        "layoutSizingVertical": "HUG",
                                        "effects": [],
                                        "interactions": [],
                                    }
                                ],
                                "blendMode": "PASS_THROUGH",
                                "clipsContent": False,
                                "background": [],
                                "fills": [],
                                "strokes": [],
                                "strokeWeight": 1.0,
                                "strokeAlign": "INSIDE",
                                "backgroundColor": {
                                    "r": 0.0,
                                    "g": 0.0,
                                    "b": 0.0,
                                    "a": 0.0,
                                },
                                "absoluteBoundingBox": {
                                    "x": 1.0,
                                    "y": -347.0,
                                    "width": 1222.0,
                                    "height": 29.0,
                                },
                                "absoluteRenderBounds": {
                                    "x": 1.0,
                                    "y": -347.0,
                                    "width": 1222.0,
                                    "height": 29.0,
                                },
                                "constraints": {
                                    "vertical": "TOP",
                                    "horizontal": "LEFT",
                                },
                                "effects": [],
                                "interactions": [],
                            },
                            {
                                "id": "1:94",
                                "name": "Text 1",
                                "type": "GROUP",
                                "scrollBehavior": "SCROLLS",
                                "children": [
                                    {
                                        "id": "1:78",
                                        "name": "Edit like a pro",
                                        "type": "TEXT",
                                        "scrollBehavior": "SCROLLS",
                                        "blendMode": "PASS_THROUGH",
                                        "fills": [
                                            {
                                                "blendMode": "NORMAL",
                                                "type": "SOLID",
                                                "color": {
                                                    "r": 1.0,
                                                    "g": 1.0,
                                                    "b": 1.0,
                                                    "a": 1.0,
                                                },
                                            }
                                        ],
                                        "strokes": [],
                                        "strokeWeight": 1.0,
                                        "strokeAlign": "OUTSIDE",
                                        "absoluteBoundingBox": {
                                            "x": 359.0,
                                            "y": -94.0,
                                            "width": 627.0,
                                            "height": 88.0,
                                        },
                                        "absoluteRenderBounds": {
                                            "x": 364.97601318359375,
                                            "y": -75.26399993896484,
                                            "width": 617.8590087890625,
                                            "height": 52.12799835205078,
                                        },
                                        "constraints": {
                                            "vertical": "TOP",
                                            "horizontal": "CENTER",
                                        },
                                        "characters": "Edit like a pro",
                                        "style": {
                                            "fontFamily": "Montserrat",
                                            "fontPostScriptName": "Montserrat-Bold",
                                            "fontWeight": 700,
                                            "textCase": "UPPER",
                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                            "fontSize": 72.0,
                                            "textAlignHorizontal": "LEFT",
                                            "textAlignVertical": "TOP",
                                            "letterSpacing": 0.0,
                                            "lineHeightPx": 87.76799774169922,
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
                                    {
                                        "id": "1:83",
                                        "name": "and make money",
                                        "type": "TEXT",
                                        "scrollBehavior": "SCROLLS",
                                        "blendMode": "PASS_THROUGH",
                                        "fills": [
                                            {
                                                "blendMode": "NORMAL",
                                                "type": "SOLID",
                                                "color": {
                                                    "r": 1.0,
                                                    "g": 1.0,
                                                    "b": 1.0,
                                                    "a": 1.0,
                                                },
                                            }
                                        ],
                                        "strokes": [],
                                        "strokeWeight": 1.0,
                                        "strokeAlign": "OUTSIDE",
                                        "absoluteBoundingBox": {
                                            "x": 343.0,
                                            "y": -24.0,
                                            "width": 658.0,
                                            "height": 88.0,
                                        },
                                        "absoluteRenderBounds": {
                                            "x": 345.66400146484375,
                                            "y": -7.424003601074219,
                                            "width": 655.147705078125,
                                            "height": 67.96800231933594,
                                        },
                                        "constraints": {
                                            "vertical": "TOP",
                                            "horizontal": "CENTER",
                                        },
                                        "characters": "and make money",
                                        "style": {
                                            "fontFamily": "Montserrat",
                                            "fontPostScriptName": "Montserrat-Bold",
                                            "fontWeight": 700,
                                            "textCase": "LOWER",
                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                            "fontSize": 72.0,
                                            "textAlignHorizontal": "LEFT",
                                            "textAlignVertical": "TOP",
                                            "letterSpacing": 0.0,
                                            "lineHeightPx": 87.76799774169922,
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
                                "blendMode": "PASS_THROUGH",
                                "clipsContent": False,
                                "background": [],
                                "fills": [],
                                "strokes": [],
                                "rectangleCornerRadii": [0.0, 0.0, 0.0, 0.0],
                                "cornerSmoothing": 0.0,
                                "strokeWeight": 1.0,
                                "strokeAlign": "INSIDE",
                                "backgroundColor": {
                                    "r": 0.0,
                                    "g": 0.0,
                                    "b": 0.0,
                                    "a": 0.0,
                                },
                                "absoluteBoundingBox": {
                                    "x": 343.0,
                                    "y": -94.0,
                                    "width": 658.0,
                                    "height": 158.0,
                                },
                                "absoluteRenderBounds": {
                                    "x": 343.0,
                                    "y": -94.0,
                                    "width": 658.0,
                                    "height": 158.0,
                                },
                                "constraints": {
                                    "vertical": "CENTER",
                                    "horizontal": "CENTER",
                                },
                                "effects": [],
                                "interactions": [],
                            },
                            {
                                "id": "1:95",
                                "name": "This is an intensive program for those who want to master the skills of professional graphic design",
                                "type": "TEXT",
                                "scrollBehavior": "SCROLLS",
                                "blendMode": "PASS_THROUGH",
                                "fills": [
                                    {
                                        "blendMode": "NORMAL",
                                        "type": "SOLID",
                                        "color": {
                                            "r": 1.0,
                                            "g": 1.0,
                                            "b": 1.0,
                                            "a": 1.0,
                                        },
                                    }
                                ],
                                "strokes": [],
                                "strokeWeight": 1.0,
                                "strokeAlign": "OUTSIDE",
                                "absoluteBoundingBox": {
                                    "x": 422.0,
                                    "y": 94.0,
                                    "width": 499.0,
                                    "height": 44.0,
                                },
                                "absoluteRenderBounds": {
                                    "x": 422.1928405761719,
                                    "y": 97.55400085449219,
                                    "width": 497.0882263183594,
                                    "height": 39.02799987792969,
                                },
                                "constraints": {
                                    "vertical": "TOP",
                                    "horizontal": "CENTER",
                                },
                                "characters": "This is an intensive program for those who \nwant to master the  skills of professional graphic design ",
                                "style": {
                                    "fontFamily": "Montserrat",
                                    "fontPostScriptName": "Montserrat-Regular",
                                    "fontWeight": 400,
                                    "textAutoResize": "WIDTH_AND_HEIGHT",
                                    "fontSize": 18.0,
                                    "textAlignHorizontal": "CENTER",
                                    "textAlignVertical": "TOP",
                                    "letterSpacing": 0.0,
                                    "lineHeightPx": 21.941999435424805,
                                    "lineHeightPercent": 100.0,
                                    "lineHeightUnit": "INTRINSIC_%",
                                },
                                "layoutVersion": 4,
                                "characterStyleOverrides": [],
                                "styleOverrideTable": {},
                                "lineTypes": ["NONE", "NONE"],
                                "lineIndentations": [0, 0],
                                "effects": [],
                                "interactions": [],
                            },
                            {
                                "id": "1:106",
                                "name": "CTA",
                                "type": "FRAME",
                                "scrollBehavior": "SCROLLS",
                                "children": [
                                    {
                                        "id": "1:107",
                                        "name": "Order",
                                        "type": "TEXT",
                                        "scrollBehavior": "SCROLLS",
                                        "blendMode": "PASS_THROUGH",
                                        "fills": [
                                            {
                                                "blendMode": "NORMAL",
                                                "type": "SOLID",
                                                "color": {
                                                    "r": 0.0,
                                                    "g": 0.0,
                                                    "b": 0.0,
                                                    "a": 1.0,
                                                },
                                            }
                                        ],
                                        "strokes": [],
                                        "strokeWeight": 1.0,
                                        "strokeAlign": "OUTSIDE",
                                        "absoluteBoundingBox": {
                                            "x": 653.0,
                                            "y": 186.0,
                                            "width": 55.0,
                                            "height": 22.0,
                                        },
                                        "absoluteRenderBounds": {
                                            "x": 654.0174560546875,
                                            "y": 189.6439971923828,
                                            "width": 53.22314453125,
                                            "height": 13.572006225585938,
                                        },
                                        "constraints": {
                                            "vertical": "CENTER",
                                            "horizontal": "CENTER",
                                        },
                                        "characters": "Order",
                                        "style": {
                                            "fontFamily": "Montserrat",
                                            "fontPostScriptName": "Montserrat-Bold",
                                            "fontWeight": 700,
                                            "textAutoResize": "WIDTH_AND_HEIGHT",
                                            "fontSize": 18.0,
                                            "textAlignHorizontal": "CENTER",
                                            "textAlignVertical": "TOP",
                                            "letterSpacing": 0.0,
                                            "lineHeightPx": 21.941999435424805,
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
                                    }
                                ],
                                "blendMode": "PASS_THROUGH",
                                "clipsContent": True,
                                "background": [
                                    {
                                        "blendMode": "NORMAL",
                                        "type": "SOLID",
                                        "color": {
                                            "r": 0.658823549747467,
                                            "g": 1.0,
                                            "b": 0.2078431397676468,
                                            "a": 1.0,
                                        },
                                    }
                                ],
                                "fills": [
                                    {
                                        "blendMode": "NORMAL",
                                        "type": "SOLID",
                                        "color": {
                                            "r": 0.658823549747467,
                                            "g": 1.0,
                                            "b": 0.2078431397676468,
                                            "a": 1.0,
                                        },
                                    }
                                ],
                                "strokes": [],
                                "cornerRadius": 40.0,
                                "cornerSmoothing": 0.0,
                                "strokeWeight": 1.0,
                                "strokeAlign": "INSIDE",
                                "backgroundColor": {
                                    "r": 0.658823549747467,
                                    "g": 1.0,
                                    "b": 0.2078431397676468,
                                    "a": 1.0,
                                },
                                "absoluteBoundingBox": {
                                    "x": 590.0,
                                    "y": 168.0,
                                    "width": 180.0,
                                    "height": 57.0,
                                },
                                "absoluteRenderBounds": {
                                    "x": 565.0,
                                    "y": 143.0,
                                    "width": 230.0,
                                    "height": 107.0,
                                },
                                "constraints": {
                                    "vertical": "CENTER",
                                    "horizontal": "CENTER",
                                },
                                "effects": [
                                    {
                                        "type": "DROP_SHADOW",
                                        "visible": True,
                                        "color": {
                                            "r": 0.658823549747467,
                                            "g": 1.0,
                                            "b": 0.2078431397676468,
                                            "a": 0.25,
                                        },
                                        "blendMode": "NORMAL",
                                        "offset": {"x": 0.0, "y": 0.0},
                                        "radius": 25.0,
                                        "showShadowBehindNode": False,
                                    }
                                ],
                                "interactions": [],
                            },
                        ],
                        "blendMode": "PASS_THROUGH",
                        "clipsContent": True,
                        "background": [
                            {
                                "blendMode": "NORMAL",
                                "type": "SOLID",
                                "color": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0},
                            }
                        ],
                        "fills": [
                            {
                                "blendMode": "NORMAL",
                                "type": "SOLID",
                                "color": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0},
                            }
                        ],
                        "strokes": [],
                        "strokeWeight": 1.0,
                        "strokeAlign": "INSIDE",
                        "backgroundColor": {"r": 1.0, "g": 1.0, "b": 1.0, "a": 1.0},
                        "layoutGrids": [
                            {
                                "pattern": "COLUMNS",
                                "sectionSize": 88.33333587646484,
                                "visible": True,
                                "color": {
                                    "r": 1.0,
                                    "g": 0.0,
                                    "b": 0.0,
                                    "a": 0.10000000149011612,
                                },
                                "alignment": "STRETCH",
                                "gutterSize": 20.0,
                                "offset": 80.0,
                                "count": 12,
                            }
                        ],
                        "absoluteBoundingBox": {
                            "x": -79.0,
                            "y": -384.0,
                            "width": 1440.0,
                            "height": 900.0,
                        },
                        "absoluteRenderBounds": {
                            "x": -79.0,
                            "y": -384.0,
                            "width": 1440.0,
                            "height": 900.0,
                        },
                        "constraints": {"vertical": "TOP", "horizontal": "LEFT"},
                        "effects": [],
                        "interactions": [],
                    },
                    {
                        "id": "1:77",
                        "name": "Main Menu",
                        "type": "FRAME",
                        "scrollBehavior": "SCROLLS",
                        "children": [
                            {
                                "id": "1:74",
                                "name": "Frame 2",
                                "type": "FRAME",
                                "scrollBehavior": "SCROLLS",
                                "children": [
                                    {
                                        "id": "1:70",
                                        "name": "bxl:instagram-alt",
                                        "type": "FRAME",
                                        "scrollBehavior": "SCROLLS",
                                        "children": [
                                            {
                                                "id": "1:71",
                                                "name": "Vector",
                                                "type": "VECTOR",
                                                "scrollBehavior": "SCROLLS",
                                                "blendMode": "PASS_THROUGH",
                                                "fills": [
                                                    {
                                                        "blendMode": "NORMAL",
                                                        "type": "SOLID",
                                                        "color": {
                                                            "r": 1.0,
                                                            "g": 1.0,
                                                            "b": 1.0,
                                                            "a": 1.0,
                                                        },
                                                    }
                                                ],
                                                "strokes": [],
                                                "strokeWeight": 1.0,
                                                "strokeAlign": "INSIDE",
                                                "absoluteBoundingBox": {
                                                    "x": 1122.0,
                                                    "y": -343.0,
                                                    "width": 18.007999420166016,
                                                    "height": 18.03799819946289,
                                                },
                                                "absoluteRenderBounds": {
                                                    "x": 1122.0,
                                                    "y": -343.0,
                                                    "width": 18.008056640625,
                                                    "height": 18.037994384765625,
                                                },
                                                "constraints": {
                                                    "vertical": "TOP",
                                                    "horizontal": "LEFT",
                                                },
                                                "layoutAlign": "INHERIT",
                                                "layoutGrow": 0.0,
                                                "layoutSizingHorizontal": "FIXED",
                                                "layoutSizingVertical": "FIXED",
                                                "effects": [],
                                                "interactions": [],
                                            },
                                            {
                                                "id": "1:72",
                                                "name": "Vector",
                                                "type": "VECTOR",
                                                "scrollBehavior": "SCROLLS",
                                                "blendMode": "PASS_THROUGH",
                                                "fills": [
                                                    {
                                                        "blendMode": "NORMAL",
                                                        "type": "SOLID",
                                                        "color": {
                                                            "r": 1.0,
                                                            "g": 1.0,
                                                            "b": 1.0,
                                                            "a": 1.0,
                                                        },
                                                    }
                                                ],
                                                "strokes": [],
                                                "strokeWeight": 1.0,
                                                "strokeAlign": "INSIDE",
                                                "absoluteBoundingBox": {
                                                    "x": 1127.990966796875,
                                                    "y": -337.0097961425781,
                                                    "width": 6.005999565124512,
                                                    "height": 6.015509605407715,
                                                },
                                                "absoluteRenderBounds": {
                                                    "x": 1127.990966796875,
                                                    "y": -337.0097961425781,
                                                    "width": 6.0059814453125,
                                                    "height": 6.0155029296875,
                                                },
                                                "constraints": {
                                                    "vertical": "SCALE",
                                                    "horizontal": "SCALE",
                                                },
                                                "layoutAlign": "INHERIT",
                                                "layoutGrow": 0.0,
                                                "layoutPositioning": "ABSOLUTE",
                                                "layoutSizingHorizontal": "FIXED",
                                                "layoutSizingVertical": "FIXED",
                                                "effects": [],
                                                "interactions": [],
                                            },
                                        ],
                                        "blendMode": "PASS_THROUGH",
                                        "clipsContent": True,
                                        "background": [
                                            {
                                                "blendMode": "NORMAL",
                                                "visible": False,
                                                "type": "SOLID",
                                                "color": {
                                                    "r": 1.0,
                                                    "g": 1.0,
                                                    "b": 1.0,
                                                    "a": 1.0,
                                                },
                                            }
                                        ],
                                        "fills": [
                                            {
                                                "blendMode": "NORMAL",
                                                "visible": False,
                                                "type": "SOLID",
                                                "color": {
                                                    "r": 1.0,
                                                    "g": 1.0,
                                                    "b": 1.0,
                                                    "a": 1.0,
                                                },
                                            }
                                        ],
                                        "strokes": [],
                                        "strokeWeight": 1.0,
                                        "strokeAlign": "INSIDE",
                                        "backgroundColor": {
                                            "r": 0.0,
                                            "g": 0.0,
                                            "b": 0.0,
                                            "a": 0.0,
                                        },
                                        "layoutMode": "HORIZONTAL",
                                        "itemSpacing": 10.0,
                                        "primaryAxisSizingMode": "FIXED",
                                        "counterAxisAlignItems": "CENTER",
                                        "paddingLeft": 3.0,
                                        "paddingRight": 3.0,
                                        "paddingTop": 3.0,
                                        "paddingBottom": 3.0,
                                        "layoutWrap": "NO_WRAP",
                                        "absoluteBoundingBox": {
                                            "x": 1119.0,
                                            "y": -346.0,
                                            "width": 24.0,
                                            "height": 24.03799819946289,
                                        },
                                        "absoluteRenderBounds": {
                                            "x": 1119.0,
                                            "y": -346.0,
                                            "width": 24.0,
                                            "height": 24.037994384765625,
                                        },
                                        "constraints": {
                                            "vertical": "TOP",
                                            "horizontal": "LEFT",
                                        },
                                        "layoutAlign": "INHERIT",
                                        "layoutGrow": 0.0,
                                        "layoutSizingHorizontal": "FIXED",
                                        "layoutSizingVertical": "HUG",
                                        "effects": [],
                                        "interactions": [],
                                    }
                                ],
                                "blendMode": "PASS_THROUGH",
                                "clipsContent": False,
                                "background": [],
                                "fills": [],
                                "strokes": [],
                                "strokeWeight": 1.0,
                                "strokeAlign": "INSIDE",
                                "backgroundColor": {
                                    "r": 0.0,
                                    "g": 0.0,
                                    "b": 0.0,
                                    "a": 0.0,
                                },
                                "layoutMode": "HORIZONTAL",
                                "itemSpacing": 10.0,
                                "counterAxisAlignItems": "CENTER",
                                "paddingLeft": 10.0,
                                "paddingRight": 10.0,
                                "paddingTop": 10.0,
                                "paddingBottom": 10.0,
                                "layoutWrap": "NO_WRAP",
                                "absoluteBoundingBox": {
                                    "x": 1109.0,
                                    "y": -356.0,
                                    "width": 44.0,
                                    "height": 44.03799819946289,
                                },
                                "absoluteRenderBounds": {
                                    "x": 1109.0,
                                    "y": -356.0,
                                    "width": 44.0,
                                    "height": 44.037994384765625,
                                },
                                "constraints": {
                                    "vertical": "TOP",
                                    "horizontal": "LEFT",
                                },
                                "layoutSizingHorizontal": "HUG",
                                "layoutSizingVertical": "HUG",
                                "effects": [],
                                "interactions": [],
                            }
                        ],
                        "blendMode": "PASS_THROUGH",
                        "clipsContent": False,
                        "background": [],
                        "fills": [],
                        "strokes": [],
                        "strokeWeight": 1.0,
                        "strokeAlign": "INSIDE",
                        "backgroundColor": {"r": 0.0, "g": 0.0, "b": 0.0, "a": 0.0},
                        "absoluteBoundingBox": {
                            "x": 1109.0,
                            "y": -356.0,
                            "width": 31.0,
                            "height": 35.0,
                        },
                        "absoluteRenderBounds": {
                            "x": 1109.0,
                            "y": -356.0,
                            "width": 44.0,
                            "height": 44.037994384765625,
                        },
                        "constraints": {"vertical": "TOP", "horizontal": "LEFT"},
                        "effects": [],
                        "interactions": [],
                    },
                ],
                "backgroundColor": {
                    "r": 0.11764705926179886,
                    "g": 0.11764705926179886,
                    "b": 0.11764705926179886,
                    "a": 1.0,
                },
                "prototypeStartNodeID": None,
                "flowStartingPoints": [],
                "prototypeDevice": {"type": "NONE", "rotation": "NONE"},
            }
        ],
    },
    "components": {},
    "componentSets": {},
    "schemaVersion": 0,
    "styles": {},
    "name": "TestApp",
    "lastModified": "2024-12-19T23:13:18Z",
    "thumbnailUrl": "https://s3-alpha.figma.com/thumbnails/99c47e1b-7c8e-4c59-a157-7c9b64c148e0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWCZ5JER5WN%2F20241219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241219T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=2174fee6130bf8e4dfda475622ead95c63c8e8c063ac3df95b0e7f96fddf5c3e",
    "version": "2163963501967374953",
    "role": "owner",
    "editorType": "figma",
    "linkAccess": "view",
}
