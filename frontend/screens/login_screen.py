# frontend/screens/login_screen.py
import flet as ft
import requests
import os


def show_login_form(page: ft.Page):
    def login_clicked(e):
        username = username_input.value
        password = password_input.value
        
        response = requests.post('http://127.0.0.1:8000/api/login/', data={
            'username': username,
            'password': password,
        })
        
        if response.status_code == 200:
            user_data = response.json()['user']
            page.clean()
            #Ir para a tela de navegacao
            go_to_nav()
            
        else:
            error_msg.value = "Usuário ou senha incorretos!"
            error_msg.update()

    def go_to_register(e):
        from screens.register_screen import show_register_form
        page.clean()
        show_register_form(page)

    def go_to_nav():
        from screens.nav_screen import show_nav
        page.clean()
        show_nav(page)

    username_input = ft.TextField(label="Usuário", width=300)
    password_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)
    login_button = ft.ElevatedButton(text="Entrar", on_click=login_clicked)
    register_button = ft.ElevatedButton(text="Registrar", on_click=go_to_register)
    error_msg = ft.Text(value="", color="red")

    # Usando caminho absoluto para a imagem
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "../assets/image.png")  # Caminho para a imagem

    background = ft.Container(
        content=ft.Column(
            [
                username_input,
                password_input,
                login_button,
                register_button,
                error_msg,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50
        ),
        expand=True,
        padding=ft.padding.all(20),
        image_src=image_path,  # Usando caminho absoluto
        image_opacity=1,
        image_fit=ft.ImageFit.COVER,
    )

    page.add(background)
