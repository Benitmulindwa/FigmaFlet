import flet as ft


def submit_data(e): ...


apikey = ft.TextField()
file_url = ft.TextField()
path = ft.TextField()


def main(page: ft.Page):
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.add(
        ft.Text("FigmaFlet", size=30, weight=ft.FontWeight.BOLD),
        ft.Column([ft.Text("API Key:"), apikey]),
        ft.Column([ft.Text("File url:"), file_url]),
        ft.Column([ft.Text("File PATH:"), path]),
        ft.TextButton("SUBMIT", ft.Icons.UPLOAD, on_click=submit_data),
    )


ft.app(target=main)
