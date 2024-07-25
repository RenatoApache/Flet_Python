from flet import *

def main(page: Page):
    
    def atualizar_agora(e):
        page.banner.open=False
        print("Atualizando...")
        page.update()

    def lembrar_mais_tarde(e):
        page.banner.open=False
        print("Vou te lembrar mais tarde...")
        page.update()

    def Cancelar(e):
        page.banner.open=False
        print("Cancelado!")
        page.update()

    page.banner=Banner(
        bgcolor=colors.AMBER_900,
        leading=Icon(icons.WARNING_OUTLINED),
        content=Text("Já temos uma atualização para esssa sua aplicação disponivel, gostaria de atualizar agora?"),
        actions=[
            TextButton("Atualizar agora", on_click=atualizar_agora),
            TextButton("Lembrar mais tarde", on_click=lembrar_mais_tarde),
            TextButton("Cancelar", on_click=Cancelar),
        ],
    )

    def abrir_banner(e):
        page.banner.open=True
        page.update()

    page.add(
        Text("Olá mundo!"),
        ElevatedButton("Executar", on_click=abrir_banner)
    )

app(target=main)