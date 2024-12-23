TEMPLATE = """
import flet as ft

def main(page: ft.Page):
    page.padding=0
    page.add(
       
        {{ element }}
        
    )
ft.app(target=main)
"""
