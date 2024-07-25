# configuração da página
import flet as ft # Importa a biblioteca Flet com o alias 'ft'

def main(page: ft.Page): # Define a função principal 'main' que recebe a página como argumento
    # Título da página
    page.title = "Aplicação teste" # Define o título da página como "Aplicação teste"
    # Tema da página
    page.theme_mode = ft.ThemeMode.DARK # Define o tema da página como escuro
    page.update() # Atualiza a página para aplicar as mudanças

ft.app(target=main) # Inicia a aplicação Flet com a função 'main' como alvo
