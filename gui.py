import sys
import os
import flet as ft
from pathlib import Path

from figmaflet.generateUI import UI


apikey = ft.TextField(hint_text="Enter your Figma API Key")
file_url = ft.TextField(hint_text="Enter the Figma file URL(project URL)")
path = ft.TextField(hint_text="Enter the output file path")


def main(page: ft.Page):
    page.theme_mode = "light"
    page.window.width = 600
    page.horizontal_alignment = "center"

    def submit_data(e):
        apikey_value = apikey.value.strip()
        file_url_value = file_url.value.strip()
        path_value = path.value.strip()

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
            page.open(ft.AlertDialog(content=ft.Text("UI generated successfully!")))
        except Exception as ex:
            page.open(ft.AlertDialog(content=ft.Text(f"An error occurred: {ex}")))

    page.add(
        ft.Text("FigmaFlet", size=30, weight=ft.FontWeight.BOLD),
        ft.Column([ft.Text("API Key:"), apikey]),
        ft.Column([ft.Text("File url:"), file_url]),
        ft.Column([ft.Text("File PATH:"), path]),
        ft.TextButton("GENERATE", ft.Icons.UPLOAD, on_click=submit_data),
    )


ft.app(target=main)
