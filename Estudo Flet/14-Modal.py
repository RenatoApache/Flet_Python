from flet import *

def main(page: Page):

    #Parte 1 - Criar o aleta
    alerta = AlertDialog(
        title=Text("Informação importante"),
        content= Text("Vida longa e prospera!"),
        on_dismiss=lambda e:print("Alerta fechada!")
    )

    #Parte 3 - Função para abrir o alerta
    def abrir_alerta(e):
        page.dialog = alerta
        alerta.open = True
        page.update()

    #Parte 2 - Criar o botão    
    page.add(
        Text("Olá Mundo!"),
        ElevatedButton("Informação", on_click=abrir_alerta)
    )    

app(target=main)