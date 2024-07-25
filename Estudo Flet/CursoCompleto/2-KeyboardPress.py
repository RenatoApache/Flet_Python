import flet as ft # Importa a biblioteca Flet com o alias 'ft'

def app(page: ft.Page): # Define a função principal 'app' que recebe a página como argumento

    def tecla(e: ft.KeyboardEvent): # Define a função 'tecla' que será chamada ao pressionar uma tecla
        page.add( # Adiciona um novo texto à página
            ft.Text(f"Tecla pressionada: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta:{e.meta}") # Mostra a tecla pressionada e os modificadores (Shift, Control, Alt, Meta)
        )        
    
    page.on_keyboard_event = tecla # Define a função 'tecla' como o manipulador de eventos de teclado
    page.add( # Adiciona um texto inicial à página
        ft.Text("Pressione qualquer tecla ou uma combinação de teclas(CTR, SHIFT, ALT, META)...") # Instruções para o usuário
    )

ft.app(target=app, view=ft.WEB_BROWSER, assets_dir="assets") # Inicia a aplicação Flet com a função 'app', visualização no navegador e diretório de assets
