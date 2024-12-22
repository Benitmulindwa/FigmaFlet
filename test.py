import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Stack(
            [
                ft.Container(
                    left=5,
                    top=5,
                    width=150,
                    height=50,
                    bgcolor="#FF0000",
                ),
                ft.Container(
                    left=40,
                    top=55,
                    width=100,
                    height=100,
                    bgcolor="#00FF00",
                ),
                ft.Container(
                    content=ft.Text(value="FletEditor", size=24.0),
                    left=9.0,
                    top=367.0,
                    width=125,
                    height=29,
                ),
            ]
        )
    )


ft.app(target=main)
