from flet import *  # Importa todos os componentes da biblioteca Flet

def main(page: Page):  # Define a função principal 'main' que recebe a página como argumento
    page.title = "Sistema de rotas"

    def mudanca_de_rota(route):
        page.views.clear()  # Limpa todas as visualizações existentes na página
        page.views.append(  # Adiciona uma nova visualização (página inicial)
            View(
                "/",
                [
                    AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT),  # Barra de aplicativo com título "Flet app"
                    ElevatedButton("Visite a liga", on_click=lambda _: page.go("/loja")),  # Botão "Visite a liga" que navega para a rota "/loja"
                ],
            )
        )

        if page.route == "/loja":  # Se a rota atual for "/loja"
            page.views.append(  # Adiciona outra visualização (página "Loja")
                View(
                    "/loja",
                    [
                        AppBar(title=Text("Loja"), bgcolor=colors.SURFACE_VARIANT),  # Barra de aplicativo com título "Loja"
                        ElevatedButton("Pagina Inicial", on_click=lambda _: page.go("/")),  # Botão "Página Inicial" que navega de volta à página inicial ("/")
                    ],
                )
            )

        page.update()  # Atualiza a página para refletir as alterações

    def view_pop(view):
        page.views.pop()  # Remove a visualização superior da pilha
        top_view = page.views[-1]  # Obtém a nova visualização superior
        page.go(top_view.route)  # Navega para a rota da nova visualização superior

    page.on_route_change = mudanca_de_rota  # Define a função 'mudanca_de_rota' como manipuladora de mudança de rota
    page.on_view_pop = view_pop  # Define a função 'view_pop' como manipuladora de remoção de visualização
    page.go(page.route)  # Navega para a rota inicial especificada por 'page.route'

app(target=main, view=WEB_BROWSER)  # Inicia a aplicação Flet com a função 'main' como alvo e visualização no navegador
