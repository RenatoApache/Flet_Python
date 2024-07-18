from flet import * #Importar a biblioteca flet

def main(page):

    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor preencha o seu nome!"
            page.update()#Função para limpar a pagina            
        elif not entrada_senha.value:
            entrada_senha.error_text = "Campo de senha obrigatório."
            page.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")

            page.clean()
            page.add(Text(f"Olá, {nome}\nSeja bem vindo a nossa aplicação!"))

    entrada_nome = TextField(label="Digite o seu nome!")
    entrada_senha = TextField(label="Digite a sua senha!")

    page.add(
        entrada_nome,
        entrada_senha,
        ElevatedButton("Clique em mim!", on_click=login)
    )
    pass

app(target=main)