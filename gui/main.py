import sys
import os
import flet as ft
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent) + "\\figmaflet")
try:
    from figmaflet.generateUI import UI
except ModuleNotFoundError:
    raise RuntimeError("Couldn't add FigmaFlet to the PATH.")

# print(str(Path(__file__).resolve().parent.parent) + "\\figmaflet")


def submit_data(e): ...


apikey = ft.TextField()
file_url = ft.TextField()
path = ft.TextField()


def main(page: ft.Page):
    page.theme_mode = "light"
    page.window.width = 600
    page.horizontal_alignment = "center"
    page.add(
        ft.Text("FigmaFlet", size=30, weight=ft.FontWeight.BOLD),
        ft.Column([ft.Text("API Key:"), apikey]),
        ft.Column([ft.Text("File url:"), file_url]),
        ft.Column([ft.Text("File PATH:"), path]),
        ft.TextButton("SUBMIT", ft.Icons.UPLOAD, on_click=submit_data),
    )


ft.app(target=main)
