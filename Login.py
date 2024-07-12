import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Página de Login"
    page.bgcolor = ft.colors.LIGHT_BLUE

    # Crie um contêiner para os widgets
    container = ft.Container(padding=20, bgcolor=ft.colors.WHITE)
    page.add(container)

    # Adicione widgets à página
    username_input = ft.TextField(hint="Nome de usuário")
    password_input = ft.TextField(hint="Senha", password=True)
    login_button = ft.ElevatedButton("Login", bgcolor=ft.colors.GREEN)

    container.add(username_input, password_input, login_button)

ft.app(target=main)