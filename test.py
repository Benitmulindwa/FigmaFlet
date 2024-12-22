import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Container(
            width=600,
            height=400,
            bgcolor="#FFFFFF",
            content=ft.Stack(
                [
                    ft.Container(
                        left=10,
                        top=20,
                        width=200,
                        height=100,
                        bgcolor="#FF0000",
                    ),
                    ft.Container(
                        width=300,
                        height=200,
                        bgcolor="#FFFFFF",
                        content=ft.Stack(
                            [
                                ft.Container(
                                    content=ft.Text(value="Nested Text", size=15.0),
                                    left=10,
                                    top=20,
                                    width=100,
                                    height=30,
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        )
    )


ft.app(target=main)
