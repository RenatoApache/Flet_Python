import flet as ft # Importa a biblioteca Flet com o alias 'ft'

def main(page: ft.Page): # Define a função principal 'main' que recebe a página como argumento
    lista = ft.ListView(spacing=2, expand=True) # Cria uma ListView com espaçamento entre os itens e que se expande para preencher o espaço disponível

    for i in range(100): # Loop que itera 100 vezes
        lista.controls.append(ft.Text(f"Estamos na linha {i}")) # Adiciona um texto à ListView para cada iteração do loop
        
        page.add(lista) # Adiciona a ListView à página

ft.app(target=main, view=ft.WEB_BROWSER) # Inicia a aplicação Flet com a função 'main', visualização no navegador e diretório de assets
