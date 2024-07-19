from flet import * # Importa todos os componentes da biblioteca Flet

def main(page: Page): # Define a função principal 'main' que recebe a página como argumento
    lv = ListView(expand=1, spacing=10, item_extent=50) # Cria uma ListView que se expande para preencher o espaço disponível, com espaçamento de 10 entre os itens e altura fixa de 50 para cada item
    page.add(lv) # Adiciona a ListView à página

    for i in range(5000): # Loop que itera 5000 vezes
        lv.controls.append( # Adiciona um texto à ListView para cada iteração do loop
            Text(f"Linha {i}") # Texto que mostra o índice da linha
        )
        if i % 100 == 0: # A cada 100 iterações
            page.update() # Atualiza a página para refletir as mudanças

    page.update() # Atualiza a página para garantir que todas as mudanças sejam refletidas

app(target=main, view=WEB_BROWSER) # Inicia a aplicação Flet com a função 'main' como alvo e visualização no navegado