import flet as ft # Importa a biblioteca Flet com o alias 'ft'

def main(page: ft.Page): # Define a função principal 'main' que recebe a página como argumento
    for i in range(500): # Loop que itera 500 vezes
        page.controls.append(ft.Text(f"Estamos na linha{i}")) # Adiciona um texto à página para cada iteração do loop
    page.scroll = "always" # Define a rolagem da página para sempre ativa
    page.update() # Atualiza a página para refletir as mudanças

ft.app(target=main) # Inicia a aplicação Flet com a função 'main' como alvo
