from flet import * # Importa todos os componentes da biblioteca Flet

def main(page: Page): # Define a função principal 'main' que recebe a página como argumento
    page.add(Text(f"Rota inicial: {page.route}")) # Adiciona um texto à página mostrando a rota inicial

    def nova_rota(route): # Define a função 'nova_rota' que será chamada quando a rota mudar
        page.add(Text(f"Nova rota: {route}")) # Adiciona um texto à página mostrando a nova rota

    def rota_compras(e): # Define a função 'rota_compras' que será chamada ao clicar no botão
        page.route = "/compras" # Define a rota da página como "/compras"
        page.update() # Atualiza a página para refletir a mudança de rota

    page.on_route_change = nova_rota # Define a função 'nova_rota' como o manipulador de eventos de mudança de rota
    page.update() # Atualiza a página para aplicar as mudanças iniciais
    page.add(ElevatedButton("Ir para compras", on_click=rota_compras)) # Adiciona um botão que chama a função 'rota_compras' ao ser clicado

app(target=main, view=WEB_BROWSER) # Inicia a aplicação Flet com a função 'main' como alvo e visualização no navegador
