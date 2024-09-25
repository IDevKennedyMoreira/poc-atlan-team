import flet as ft
from screens.login_screen import show_login_form

def main(page: ft.Page):
    page.window_width = 375
    page.window_height = 667
    show_login_form(page)

ft.app(target=main)