TEMPLATE = """
import flet as ft

def main(page: ft.Page):
    page.padding=0
    page.add(
       ft.Stack([
        {{ element }}
        ])
    )
ft.app(target=main)
"""
