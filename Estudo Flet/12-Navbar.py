from flet import *

def main(page: Page):
    # Define o título da página como "Rotas"
    page.title = "Rotas"

    # Configura a barra de navegação com três destinos: Home, Explorar e Rotas
    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME, label="Home",),
            NavigationDestination(icon=icons.EXPLORE, label="Explorar"),
            NavigationDestination(icon=icons.COMMUTE, label="Rotas"),
        ]
    )

    # Adiciona um componente de texto e dois botões elevados à página
    page.add(
        Text("Corpo da aplicação"), 
        Row(
            [
                ElevatedButton(
                text="Fazer viagem", 
                icon="pause", 
                icon_color="green400"
                ), 
                IconButton(
                icon=icons.DELETE_FOREVER_ROUNDED,
                icon_color="pink600",
                icon_size=40,
                tooltip="Delete record",
                )
            ]
        )
    )

# Inicializa o aplicativo Flet, usando a função 'main' como ponto de entrada
app(target=main)

