from jinja2 import Template
from figma.template import TEMPLATE
from figma.vector_elements import Frame
from figma import endpoints


class UI:
    def __init(self, token: str, file_key: str, local_path: str):

        self.figma_file = endpoints.Files(token, file_key)
        self.file_data = self.figma_file.get_file()
        self.local_path = local_path

    # def to_code(self):

    #     # Generate Flet code for each frame
    #     elements = [frame.to_code() for frame in frames]

    #     # Render the template
    #     template = Template(TEMPLATE)
    #     rendered_code = template.render(elements=elements)
    #     return rendered_code


def main(): ...


if __name__ == "__main__":
    main()
