import os # Importa a biblioteca os para manipulação de variáveis de ambiente e operações do sistema
from flet import * # Importa todos os componentes da biblioteca Flet

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000" # Define o tamanho máximo da mensagem WebSocket para 8 MB

def main(page: Page): # Define a função principal 'main' que recebe a página como argumento
    gv = GridView(expand=True, max_extent=150, child_aspect_ratio=1) # Cria um GridView que se expande para preencher o espaço disponível, com cada item tendo um tamanho máximo de 150 e uma proporção de aspecto de 1:1
    page.add(gv) # Adiciona o GridView à página

    for i in range(1000): # Loop que itera 1000 vezes
        gv.controls.append( # Adiciona um Container ao GridView para cada iteração do loop
            Container(
                Text(f"Item {i}", size=80, color="#001188"), # Adiciona um texto ao Container com o índice do item, tamanho da fonte 80 e cor azul
                alignment=alignment.center, # Alinha o conteúdo do Container ao centro
                bgcolor=colors.AMBER_100, # Define a cor de fundo do Container como âmbar claro
                border=border.all(2, colors.AMBER_500), # Adiciona uma borda ao Container com espessura de 2 e cor âmbar
                border_radius=border_radius.all(8) # Define o raio da borda do Container como 8 para arredondar os cantos
            )
        )
    page.update() # Atualiza a página para refletir as mudanças

app(target=main, view=WEB_BROWSER) # Inicia a aplicação Flet com a função 'main' como alvo e visualização no navegador
