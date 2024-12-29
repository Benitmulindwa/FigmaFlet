TEMPLATE = """
import flet as ft

def main(page: ft.Page):
    page.padding=0
    page.add(
       ft.Stack([
        {{ elements }}
        ])
    )
ft.app(target=main)
"""
