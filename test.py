# import flet as ft


# def main(page: ft.Page):
#     page.padding = 0
#     page.add(
#         ft.Stack(
#             [
#                 ft.Container(
#                     width=1440,
#                     height=900,
#                     bgcolor="#FFFFFF",
#                     content=ft.Stack(
#                         [
#                             ft.Container(
#                                 left=0.0,
#                                 top=0.0,
#                                 width=1440.0,
#                                 height=900.0,
#                                 bgcolor="#000000",
#                             ),
#                             ft.Container(
#                                 width=1222,
#                                 height=29,
#                                 bgcolor="transparent",
#                                 content=ft.Stack(
#                                     [
#                                         ft.Container(
#                                             width=1222,
#                                             height=29,
#                                             bgcolor="transparent",
#                                             content=ft.Stack(
#                                                 [
#                                                     ft.Container(
#                                                         content=ft.Text(
#                                                             value="FletEditor",
#                                                             size=24.0,
#                                                             color="#FFFFFF",
#                                                         ),
#                                                         left=0.0,
#                                                         top=0.0,
#                                                         # width=125.0,
#                                                         # height=29.0,
#                                                     ),
#                                                     ft.Container(
#                                                         width=463,
#                                                         height=22,
#                                                         bgcolor="transparent",
#                                                         content=ft.Stack(
#                                                             [
#                                                                 ft.Container(
#                                                                     content=ft.Text(
#                                                                         value="Main",
#                                                                         size=18.0,
#                                                                         color="#FFFFFF",
#                                                                     ),
#                                                                     left=0.0,
#                                                                     top=0.0,
#                                                                     # width=46.0,
#                                                                     # height=22.0,
#                                                                 ),
#                                                                 ft.Container(
#                                                                     content=ft.Text(
#                                                                         value="About",
#                                                                         size=18.0,
#                                                                         color="#FFFFFF",
#                                                                     ),
#                                                                     left=86.0,
#                                                                     top=0.0,
#                                                                     # width=57.0,
#                                                                     # height=22.0,
#                                                                 ),
#                                                                 ft.Container(
#                                                                     content=ft.Text(
#                                                                         value="Program",
#                                                                         size=18.0,
#                                                                         color="#FFFFFF",
#                                                                     ),
#                                                                     left=183.0,
#                                                                     top=0.0,
#                                                                     # width=80.0,
#                                                                     # height=22.0,
#                                                                 ),
#                                                                 ft.Container(
#                                                                     content=ft.Text(
#                                                                         value="Price",
#                                                                         size=18.0,
#                                                                         color="#FFFFFF",
#                                                                     ),
#                                                                     left=303.0,
#                                                                     top=0.0,
#                                                                     # width=47.0,
#                                                                     # height=22.0,
#                                                                 ),
#                                                                 ft.Container(
#                                                                     content=ft.Text(
#                                                                         value="Contact",
#                                                                         size=18.0,
#                                                                         color="#FFFFFF",
#                                                                     ),
#                                                                     left=390.0,
#                                                                     top=0.0,
#                                                                     # width=73.0,
#                                                                     # height=22.0,
#                                                                 ),
#                                                             ]
#                                                         ),
#                                                     ),
#                                                     ft.Container(
#                                                         width=68,
#                                                         height=20,
#                                                         bgcolor="transparent",
#                                                         content=ft.Stack(
#                                                             [
#                                                                 ft.Container(
#                                                                     left=0.0,
#                                                                     top=0.0,
#                                                                     width=20.0,
#                                                                     height=20.0,
#                                                                     bgcolor="pink",
#                                                                 ),
#                                                                 ft.Container(
#                                                                     left=30.0,
#                                                                     top=1.0,
#                                                                     width=18.0,
#                                                                     height=18.0,
#                                                                     bgcolor="pink",
#                                                                 ),
#                                                             ]
#                                                         ),
#                                                     ),
#                                                 ]
#                                             ),
#                                         ),
#                                     ]
#                                 ),
#                             ),
#                             ft.Container(
#                                 left=343 + 79,
#                                 top=94,
#                                 width=658,
#                                 height=158,
#                                 bgcolor="transparent",
#                                 content=ft.Stack(
#                                     [
#                                         ft.Container(
#                                             content=ft.Text(
#                                                 value="EDIT LIKE A PRO",
#                                                 size=72.0,
#                                                 color="#FFFFFF",
#                                             ),
#                                             left=16.0,
#                                             top=0.0,
#                                             # width=627.0,
#                                             # height=88.0,
#                                         ),
#                                         ft.Container(
#                                             content=ft.Text(
#                                                 value="and make money",
#                                                 size=72.0,
#                                                 color="#FFFFFF",
#                                             ),
#                                             left=0.0,
#                                             top=70.0,
#                                             # width=658.0,
#                                             # height=88.0,
#                                         ),
#                                     ]
#                                 ),
#                             ),
#                             ft.Container(
#                                 content=ft.Text(
#                                     value="""This is an intensive program for those who
# want to master the  skills of professional graphic design""",
#                                     size=18.0,
#                                     color="#FFFFFF",
#                                 ),
#                                 left=501.0,
#                                 top=478.0,
#                                 # width=499.0,
#                                 # height=44.0,
#                             ),
#                             ft.Container(
#                                 width=180,
#                                 height=57,
#                                 bgcolor="#A8FF35",
#                                 content=ft.Stack(
#                                     [
#                                         ft.Container(
#                                             content=ft.Text(
#                                                 value="Order",
#                                                 size=18.0,
#                                                 color="#000000",
#                                             ),
#                                             left=63.0,
#                                             top=18.0,
#                                             # width=55.0,
#                                             # height=22.0,
#                                         ),
#                                     ]
#                                 ),
#                             ),
#                         ]
#                     ),
#                 )
#             ]
#         )
#     )


# ft.app(target=main)

# =================================================================
import flet as ft


def main(page: ft.Page):
    page.padding = 0
    page.add(
        ft.Stack(
            [
                ft.Container(
                    left=0,
                    top=0,
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
                                left=-78,
                                top=-37,
                                width=1222,
                                height=29,
                                bgcolor="transparent",
                                content=ft.Stack(
                                    [
                                        ft.Container(
                                            left=0,
                                            top=0,
                                            width=1222,
                                            height=29,
                                            bgcolor="transparent",
                                            content=ft.Stack(
                                                [
                                                    ft.Container(
                                                        content=ft.Text(
                                                            value="FletEditor",
                                                            size=24.0,
                                                            color="#FFFFFF",
                                                        ),
                                                        left=0.0,
                                                        top=0.0,
                                                    ),
                                                    ft.Container(
                                                        left=408,
                                                        top=-4,
                                                        width=463,
                                                        height=22,
                                                        bgcolor="transparent",
                                                        content=ft.Stack(
                                                            [
                                                                ft.Container(
                                                                    content=ft.Text(
                                                                        value="Main",
                                                                        size=18.0,
                                                                        color="#FFFFFF",
                                                                    ),
                                                                    left=0.0,
                                                                    top=0.0,
                                                                ),
                                                                ft.Container(
                                                                    content=ft.Text(
                                                                        value="About",
                                                                        size=18.0,
                                                                        color="#FFFFFF",
                                                                    ),
                                                                    left=86.0,
                                                                    top=0.0,
                                                                ),
                                                                ft.Container(
                                                                    content=ft.Text(
                                                                        value="Program",
                                                                        size=18.0,
                                                                        color="#FFFFFF",
                                                                    ),
                                                                    left=183.0,
                                                                    top=0.0,
                                                                ),
                                                                ft.Container(
                                                                    content=ft.Text(
                                                                        value="Price",
                                                                        size=18.0,
                                                                        color="#FFFFFF",
                                                                    ),
                                                                    left=303.0,
                                                                    top=0.0,
                                                                ),
                                                                ft.Container(
                                                                    content=ft.Text(
                                                                        value="Contact",
                                                                        size=18.0,
                                                                        color="#FFFFFF",
                                                                    ),
                                                                    left=390.0,
                                                                    top=0.0,
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    ft.Container(
                                                        left=1154,
                                                        top=-5,
                                                        width=68,
                                                        height=20,
                                                        bgcolor="transparent",
                                                        content=ft.Stack(
                                                            [
                                                                ft.Container(
                                                                    left=0.0,
                                                                    top=0.0,
                                                                    width=20.0,
                                                                    height=20.0,
                                                                    bgcolor="pink",
                                                                ),
                                                                ft.Container(
                                                                    left=30.0,
                                                                    top=1.0,
                                                                    width=18.0,
                                                                    height=18.0,
                                                                    bgcolor="pink",
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
                                left=264,
                                top=-290,
                                width=658,
                                height=158,
                                bgcolor="transparent",
                                content=ft.Stack(
                                    [
                                        ft.Container(
                                            content=ft.Text(
                                                value="EDIT LIKE A PRO",
                                                size=72.0,
                                                color="#FFFFFF",
                                            ),
                                            left=16.0,
                                            top=0.0,
                                        ),
                                        ft.Container(
                                            content=ft.Text(
                                                value="and make money",
                                                size=72.0,
                                                color="#FFFFFF",
                                            ),
                                            left=0.0,
                                            top=70.0,
                                        ),
                                    ]
                                ),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    value="""This is an intensive program for those who
want to master the  skills of professional graphic design""",
                                    size=18.0,
                                    color="#FFFFFF",
                                ),
                                left=501.0,
                                top=478.0,
                            ),
                            ft.Container(
                                left=511,
                                top=-216,
                                width=180,
                                height=57,
                                bgcolor="#A8FF35",
                                content=ft.Stack(
                                    [
                                        ft.Container(
                                            content=ft.Text(
                                                value="Order",
                                                size=18.0,
                                                color="#000000",
                                            ),
                                            left=63.0,
                                            top=18.0,
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    ),
                )
            ]
        )
    )


ft.app(target=main)
