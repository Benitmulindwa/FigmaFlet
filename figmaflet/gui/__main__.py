import re
import flet as ft
from pathlib import Path
from figmaflet.generateUI import UI


# TODO: - Redesign the gui UI, make it more beautiful and add a logo


# Extract file key from figma URL
def extract_file_key(url):

    match = re.search(r"/design/([a-zA-Z0-9]+)", url)
    if match:
        return match.group(1)
    return None


apikey = ft.TextField(label="API Token", border_radius=30, bgcolor="grey100")
file_url = ft.TextField(label="File URL", border_radius=30, bgcolor="grey100")
path = ft.TextField(label="Output PATH", border_radius=30, bgcolor="grey100")


def main(page: ft.Page):
    page.title = "FigmaFlet"
    page.theme_mode = "light"
    page.window.width = 600
    page.spacing = 30
    page.horizontal_alignment = "center"

    def submit_data(e):
        apikey_value = apikey.value.strip()
        url_value = file_url.value.strip()
        path_value = path.value.strip()

        # Extract the file key from the provided URL
        file_url_value = extract_file_key(url_value)

        # Validate input
        if not apikey_value or not file_url_value or not path_value:
            page.open(ft.AlertDialog(content=ft.Text("All fields are required!")))
            return

        # Ensure the path exists
        output_path = Path(path_value)
        if not output_path.exists():
            page.open(ft.AlertDialog(content=ft.Text("Invalid file path!")))
            return

        # Generate the Flet `UI`
        try:
            ui_generator = UI(apikey_value, file_url_value, output_path)
            ui_generator.generate()
            page.open(
                ft.AlertDialog(
                    content=ft.Text(
                        "UI generated successfully!", size=20, color="green"
                    )
                )
            )
        except Exception as ex:
            page.open(
                ft.AlertDialog(content=ft.Text(f"An error occurred: {ex}", color="red"))
            )

    page.add(
        ft.Column(
            [
                ft.Text("FigmaFlet", size=30, weight=ft.FontWeight.BOLD),
                ft.Text(
                    "Generate Flet UIs from Figma Designs",
                    size=18,
                    weight=ft.FontWeight.W_500,
                ),
            ],
            horizontal_alignment="center",
        ),
        ft.Column(
            [
                apikey,
                file_url,
                path,
                ft.ElevatedButton("GENERATE", ft.Icons.UPLOAD, on_click=submit_data),
            ],
            horizontal_alignment="center",
            spacing=25,
        ),
    )


ft.app(target=main)
