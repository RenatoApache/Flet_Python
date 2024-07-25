from flet import *

def main(page: Page):
    def confirma(e):
        alerta_dialogo.open = False
        print("Item apagado com sucesso!"),
        page.update()
        
    def cancelar(e):
        alerta_dialogo.open = False
        print("Cancelado com sucesso!"),
        page.update()

    # Criar alerta de dialogo
    alerta_dialogo = AlertDialog(
        modal=True,
        title=Text("Confirme a ação!"),
        content=Text("Deseja mesmo apagar os itens?\nSe continuar não terá mais volta!"),
        actions=[
            TextButton("Apagar", on_click=confirma),
            TextButton("Cancelar", on_click=cancelar)
        ],
        actions_alignment=MainAxisAlignment.END
    )

    def abrir_modal(e):
        page.dialog = alerta_dialogo
        alerta_dialogo.open = True
        page.update()

    page.add(
        Text("Olá mundo!"),
        ElevatedButton("Apagar item", icon=icons.DELETE, icon_color="red", on_click=abrir_modal)
    )

app(target=main)