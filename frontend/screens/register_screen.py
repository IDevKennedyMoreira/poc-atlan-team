# frontend/screens/register_screen.py
import flet as ft
import requests
import time
from screens.login_screen import show_login_form
import os

def show_register_form(page: ft.Page):
    def register_clicked(e):
        username = username_input.value
        email = email_input.value
        password = password_input.value
        confirm_password = confirm_password_input.value

        if password != confirm_password:
            register_error_msg.value = "As senhas não coincidem!"
            register_error_msg.update()
            return

        response = requests.post('http://127.0.0.1:8000/api/register/', data={
            'username': username,
            'email': email,
            'password': password,
        })
        
        if response.status_code == 200:
            user_data = response.json()['user']
            page.clean()
            page.add(ft.Text(f"Registro realizado com sucesso para o usuário {user_data['username']}!", size=10))
            time.sleep(2)
            page.add(ft.Text(f"Redirecionando para login", size=10))
            time.sleep(2)
            page.clean()
            show_login_form(page)
        else:
            register_error_msg.value = "Erro ao registrar!"
            register_error_msg.update()
    
    def go_to_login(e):
        from screens.login_screen import show_login_form
        page.clean()
        show_login_form(page)

    username_input = ft.TextField(label="Usuário", width=300)
    email_input = ft.TextField(label="E-mail", width=300)
    password_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)
    confirm_password_input = ft.TextField(label="Repetir Senha", password=True, can_reveal_password=True, width=300)
    register_button = ft.ElevatedButton(text="Registrar", on_click=register_clicked)
    back_button = ft.ElevatedButton(text="voltar", on_click=go_to_login)
    register_error_msg = ft.Text(value="", color="red")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "../assets/image.png")


    background = ft.Container(
        content=ft.Column(
            [
            username_input,
            email_input,
            password_input,
            confirm_password_input,
            register_button,
            back_button,
            register_error_msg,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50  # Espaçamento maior entre os elementos
        ),
        expand=True,
        padding=ft.padding.all(20),
        image_src=image_path,  # Usando caminho absoluto
        image_opacity=0.1,  # Ajustando a opacidade
        image_fit=ft.ImageFit.COVER,  # Usando COVER para preencher o container
        bgcolor=ft.colors.BLACK  # Fundo para garantir que o texto fique legível
    )

    page.add(background)
