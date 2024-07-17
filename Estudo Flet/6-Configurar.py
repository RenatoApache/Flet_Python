#configuração da pagina
import flet as ft

def main(page:ft.Page):
    #Titulo da pagina
    page.title = "Aplicação teste"    
    #Tema da pagina
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

ft.app(target=main)