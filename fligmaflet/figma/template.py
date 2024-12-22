TEMPLATE = """
import flet as ft

def main(page: ft.Page):
    page.add(
       ft.Stack([ {% for element in elements %}
        {{element}}
        {% endfor %}])
    )
"""
