from jinja2 import Template
from figmaflet.template import TEMPLATE
from figmaflet.figma.frame import Frame
from figmaflet.figma import endpoints
from figmaflet.figma.vector_elements import Text
from figmaflet.utils import get_fonts_urls
from pathlib import Path


class UI:
    def __init__(self, token: str, file_key: str, local_path: Path):

        self.figma_file = endpoints.Files(token, file_key)
        self.file_data = self.figma_file.get_file()
        self.local_path = local_path

        self.font_families = set()

    def to_code(self):

        # Generate Flet code for each frame
        for f in self.file_data["document"]["children"][0]["children"]:
            frame = Frame(f, figma_file=self.figma_file, output_path=self.local_path)
            # frames.append(frame.to_code())

            # Collect font URLs from frame elements
            self.collect_font_families(frame)

            font_list = [get_fonts_urls(family) for family in self.font_families]
            font_urls = {
                item.split(":")[0]: "https:" + item.split(":")[2] for item in font_list
            }

            # Render the template
            t = Template(TEMPLATE)
            rendered_code = t.render(elements=frame.to_code(), font_urls=font_urls)
            return rendered_code

    def collect_font_families(self, frame):
        for element in frame.elements:
            if isinstance(element, Text):
                self.font_families.add(element.font_family)
            elif isinstance(element, Frame):
                # Recursively collect from nested frames
                self.collect_font_families(element)

    def generate(self):
        code = self.to_code()
        self.local_path.joinpath("main.py").write_text(code, encoding="UTF-8")
