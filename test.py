import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Container(
            width=1440,
            height=900,
            bgcolor="#FFFFFF",
            content=ft.Stack(
                [
                    ft.Container(
                        left=0.0,
                        top=0.0,
                        width=1440.0,
                        height=900.0,
                        bgcolor="#000000",
                    ),
                    ft.Container(
                        width=1222,
                        height=29,
                        bgcolor="#FFFFFF",
                        content=ft.Stack(
                            [
                                ft.Container(
                                    width=1222,
                                    height=29,
                                    bgcolor="#FFFFFF",
                                    content=ft.Stack(
                                        [
                                            ft.Container(
                                                content=ft.Text(
                                                    value="FletEditor", size=24.0
                                                ),
                                                left=0.0,
                                                top=0.0,
                                                width=125.0,
                                                height=29.0,
                                            ),
                                            ft.Container(
                                                width=463,
                                                height=22,
                                                bgcolor="#FFFFFF",
                                                content=ft.Stack(
                                                    [
                                                        ft.Container(
                                                            content=ft.Text(
                                                                value="Main", size=18.0
                                                            ),
                                                            left=0.0,
                                                            top=0.0,
                                                            width=46.0,
                                                            height=22.0,
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text(
                                                                value="About", size=18.0
                                                            ),
                                                            left=86.0,
                                                            top=0.0,
                                                            width=57.0,
                                                            height=22.0,
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text(
                                                                value="Program",
                                                                size=18.0,
                                                            ),
                                                            left=183.0,
                                                            top=0.0,
                                                            width=80.0,
                                                            height=22.0,
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text(
                                                                value="Price", size=18.0
                                                            ),
                                                            left=303.0,
                                                            top=0.0,
                                                            width=47.0,
                                                            height=22.0,
                                                        ),
                                                        ft.Container(
                                                            content=ft.Text(
                                                                value="Contact",
                                                                size=18.0,
                                                            ),
                                                            left=390.0,
                                                            top=0.0,
                                                            width=73.0,
                                                            height=22.0,
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            ft.Container(
                                                width=68,
                                                height=20,
                                                bgcolor="#FFFFFF",
                                                content=ft.Stack(
                                                    [
                                                        ft.Container(
                                                            left=0.0,
                                                            top=0.0,
                                                            width=20.0,
                                                            height=20.0,
                                                            bgcolor="#000000",
                                                        ),
                                                        ft.Container(
                                                            left=30.0,
                                                            top=1.0,
                                                            width=18.0,
                                                            height=18.0,
                                                            bgcolor="#000000",
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    ft.Container(
                        left=422.0,
                        top=290.0,
                        width=658.0,
                        height=158.0,
                        bgcolor="#000000",
                    ),
                    ft.Container(
                        content=ft.Text(
                            value="""This is an intensive program for those who
want to master the  skills of professional graphic design""",
                            size=18.0,
                        ),
                        left=501.0,
                        top=478.0,
                        width=499.0,
                        height=44.0,
                    ),
                    ft.Container(
                        width=180,
                        height=57,
                        bgcolor="#A8FF35",
                        content=ft.Stack(
                            [
                                ft.Container(
                                    content=ft.Text(value="Order", size=18.0),
                                    left=63.0,
                                    top=18.0,
                                    width=55.0,
                                    height=22.0,
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
        ft.Container(
            width=31,
            height=35,
            bgcolor="#FFFFFF",
            content=ft.Stack(
                [
                    ft.Container(
                        width=44,
                        height=44,
                        bgcolor="#FFFFFF",
                        content=ft.Stack(
                            [
                                ft.Container(
                                    width=24,
                                    height=24,
                                    bgcolor="#FFFFFF",
                                    content=ft.Stack(
                                        [
                                            ft.Container(
                                                left=3.0,
                                                top=3.0,
                                                width=18.007999420166016,
                                                height=18.03799819946289,
                                                bgcolor="#000000",
                                            ),
                                            ft.Container(
                                                left=8.990966796875,
                                                top=8.990203857421875,
                                                width=6.005999565124512,
                                                height=6.015509605407715,
                                                bgcolor="#000000",
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    )


ft.app(target=main)
