from jinja2 import Template
from template import TEMPLATE
from figma.frame import Frame
from figma import endpoints
from pathlib import Path


class UI:
    def __init__(self, token: str, file_key: str, local_path: Path):

        self.figma_file = endpoints.Files(token, file_key)
        self.file_data = self.figma_file.get_file()
        self.local_path = local_path

    def to_code(self):
        # frames = []
        # Generate Flet code for each frame

        for f in self.file_data["document"]["children"][0]["children"]:
            frame = Frame(f)
            # frames.append(frame)
            # Render the template
            t = Template(TEMPLATE)
            rendered_code = t.render(elements=frame.to_code())
            return rendered_code

    def generate_file(self):
        code = self.to_code()
        self.local_path.joinpath("main.py").write_text(code, encoding="UTF-8")


# Code Example
# def main():

#     ui = UI(
#         token="FIGMA_API",
#         file_key="6EbpTUSXvrpqZb2WrtihV1",
#         local_path=Path("d:/projects/figmaflet/gui"),
#     )
#     print(ui.to_code())
#     ui.generate_file()


# if __name__ == "__main__":
#     main()
