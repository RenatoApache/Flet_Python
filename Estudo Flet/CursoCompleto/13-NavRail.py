from flet import *

def main(page: Page):
    # Define o título da página como "NavRail"
    page.title = "NavRail"

    # Cria um componente de barra de navegação lateral
    rail = NavigationRail(
        selected_index=0,  # Índice inicialmente selecionado na barra de navegação
        min_width=100,  # Largura mínima da barra de navegação
        min_extended_width=400,  # Largura mínima quando a barra de navegação está estendida
        label_type=NavigationRailLabelType.ALL,  # Exibe todos os rótulos de destino
        leading=FloatingActionButton(icon=icons.CREATE, text="Criar"),  # Botão flutuante com ícone de criação
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER,  # Ícone para o destino "Favoritar"
                selected_icon=icons.FAVORITE,  # Ícone selecionado para o destino "Favoritar"
                label="Favoritar"  # Rótulo do destino "Favoritar"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),  # Ícone de conteúdo para o destino "Marca"
                selected_icon_content=Icon(icons.BOOKMARK),  # Ícone de conteúdo selecionado para o destino "Marca"
                label="Marca"  # Rótulo do destino "Marca"
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,  # Ícone para o destino "Definições"
                selected_icon=icons.SETTINGS,  # Ícone selecionado para o destino "Definições"
                label="Definições"  # Rótulo do destino "Definições"
            )
        ],

        on_change=lambda e: print("Página Selecionada:", e.control.selected_index),  # Função de retorno de chamada
    )

    # Adiciona os componentes à página
    page.add(
        Row(
            [
                rail,  # Barra de navegação lateral
                VerticalDivider(width=1),  # Divisor vertical
                Column([Text("Corpo da aplicação")], alignment=MainAxisAlignment.START, expand=True)  # Texto do corpo da aplicação
            ],
            expand=True
        )
    )

# Inicializa o aplicativo Flet, usando a função 'main' como ponto de entrada
app(target=main)
