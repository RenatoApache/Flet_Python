from flet import *

def main(page:Page):    
    page.appbar = AppBar(# Criação da barra de aplicativo (app bar)
        leading=Icon(icons.CODE_OFF),  # Ícone "adicionar" à esquerda
        bgcolor="#003377",  # Cor de fundo da barra
        title=Text("Minha Loja"),  # Título da barra
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED, icon_color=colors.WHITE),  # Botão com ícone "sunny"
            IconButton(icons.MENU, icon_color=colors.WHITE), # Botão com ícone "Menu"
            IconButton(icon=icons.SEARCH, icon_color=colors.WHITE), # Botão com ícone "Procura"
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Logar"),  # Item de menu "Logar"
                    PopupMenuItem(text="Cadastro"),  # Item de menu vazio
                    PopupMenuItem(text="Sair")  # Item de menu "Sair"
                ]
            )
        ]
    )
    
    page.add(Text("Corpo!"))# Adiciona um widget de texto ao corpo da página

app(target=main) #Inicializa o aplicativo Flet, usando a função 'main' como ponto de entrada
