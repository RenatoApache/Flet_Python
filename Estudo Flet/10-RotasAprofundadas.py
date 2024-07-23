from flet import * # Importa todos os componentes da biblioteca Flet


def main(page: Page): # Define a função principal 'main' que recebe a página como argumento
    page.title = "Sistema de rotas"

    def mudanca_de_rota(route):
        page.view.clear()
        page.view.append(            
            View(
                "/",
                [
                    AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Visite a liga", on_click=lambda _: page.route("/loja"))
                ]
            )
        )

        if page.route == "/loja":
            page.views.append(
                View(
                  "/loja",
                  [
                      AppBar(title=Text("Loja"), bgcolor=colors.SURFACE_VARIANT),
                      ElevatedButton("Pagina Inicial", on_click=lambda _: page.route("/"))
                  ]
                )  
            )
        
        page.update()

        def view_pop (view):
            page.views.pop()
            top_view = page.viwes[-1]
            page.go(top_view.route)        

    page.on_route_change = mudanca_de_rota
app(target=main, view=WEB_BROWSER) # Inicia a aplicação Flet com a função 'main' como alvo e visualização no navegador
