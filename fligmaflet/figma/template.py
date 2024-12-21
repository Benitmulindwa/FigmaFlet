template = """
from flet import Container, Page

def main(page: Page):
    page.add(
        {% for element in elements %}
        Container(
            left={{ element.x }},
            top={{ element.y }},
            width={{ element.width }},
            height={{ element.height }},
            bgcolor="{{ element.color }}"
        ),
        {% endfor %}
    )
"""
