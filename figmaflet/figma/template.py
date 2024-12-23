TEMPLATE = """
import flet as ft

def main(page: ft.Page):
    page.add(
       
        {{ element }}
        
    )
ft.app(target=main)
"""
