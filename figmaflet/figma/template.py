TEMPLATE = """
import flet as ft

def main(page: ft.Page):
    page.add(
       {% for element in elements %}
        {{ element }}
        {% endfor %}
    )
ft.app(target=main)
"""
