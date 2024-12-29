from jinja2 import Template
from figma.template import TEMPLATE
from figma.frame import Frame
from figma import endpoints


class UI:
    def __init__(self, token: str, file_key: str, local_path: str):

        self.figma_file = endpoints.Files(token, file_key)
        self.file_data = self.figma_file.get_file()
        self.local_path = local_path

    def to_code(self):
        frames = []
        # Generate Flet code for each frame

        for f in self.file_data["document"]["children"][0]["children"]:
            frame = Frame(f)
            frames.append(frame)
            # Render the template
            t = Template(TEMPLATE)
            rendered_code = t.render(elements=frame.to_code())
            return rendered_code


# Code Example
def main():

    ui = UI(
        token="FIGMA-API",
        file_key="6EbpTUSXvrpqZb2WrtihV1",
        local_path="d:/projects/figmaflet",
    )
    print(ui.to_code())


if __name__ == "__main__":
    main()
