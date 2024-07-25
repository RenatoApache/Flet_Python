from flet import * # Importa todos os componentes da biblioteca Flet

def main(page): # Define a função principal que recebe a página como argumento

    def login(e): # Define a função de login que será chamada ao clicar no botão
        if not entrada_nome.value: # Verifica se o campo de nome está vazio
            entrada_nome.error_text = "Por favor preencha o seu nome!" # Define uma mensagem de erro
            page.update() # Atualiza a página para mostrar a mensagem de erro
        elif not entrada_senha.value: # Verifica se o campo de senha está vazio
            entrada_senha.error_text = "Campo de senha obrigatório." # Define uma mensagem de erro
            page.update() # Atualiza a página para mostrar a mensagem de erro
        else: # Se ambos os campos estiverem preenchidos
            nome = entrada_nome.value # Obtém o valor do campo de nome
            senha = entrada_senha.value # Obtém o valor do campo de senha
            print(f"Nome: {nome}\nSenha: {senha}") # Imprime o nome e a senha no console

            page.clean() # Limpa a página
            page.add(Text(f"Olá, {nome}\nSeja bem vindo a nossa aplicação!")) # Adiciona uma mensagem de boas-vindas na página

    entrada_nome = TextField(label="Digite o seu nome!") # Cria um campo de texto para o nome
    entrada_senha = TextField(label="Digite a sua senha!") # Cria um campo de texto para a senha

    page.add( # Adiciona os componentes à página
        entrada_nome, # Adiciona o campo de texto do nome
        entrada_senha, # Adiciona o campo de texto da senha
        ElevatedButton("Clique em mim!", on_click=login) # Adiciona um botão que chama a função de login ao ser clicado
    )
    pass # Declaração de passagem (não faz nada, mas é necessária para a sintaxe)

app(target=main) # Inicia a aplicação chamando a função principal
