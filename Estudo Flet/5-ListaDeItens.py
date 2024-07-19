import os  # Importa o módulo 'os' para interagir com o sistema operacional
import flet as ft  # Importa o módulo 'flet' para criar a interface gráfica

# Define o tamanho máximo da mensagem WebSocket para 8 MB
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

# Função principal que será chamada ao iniciar o aplicativo
def main(page: ft.page):
    # Cria uma linha (Row) que pode ser expandida, com rolagem sempre ativa e permite quebra de linha
    linha = ft.Row(wrap=True, scroll="always", expand=True)
    # Adiciona a linha criada à página
    page.add(linha)

    # Loop para adicionar 100 itens à linha
    for i in range(100):
        # Adiciona um contêiner (Container) à linha, com um texto, dimensões e estilos definidos
        linha.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),  # Texto exibido no contêiner
                width=100,  # Largura do contêiner
                height=100,  # Altura do contêiner
                alignment=ft.alignment.center,  # Alinhamento do texto no centro do contêiner
                bgcolor=ft.colors.AMBER_100,  # Cor de fundo do contêiner
                border=ft.border.all(2, ft.colors.AMBER_600),  # Borda do contêiner com espessura de 2 e cor definida
                border_radius=ft.border_radius.all(8)  # Raio da borda para arredondar os cantos
            )
        )
    
    # Atualiza a página para refletir as mudanças
    page.update()

# Inicia o aplicativo chamando a função 'main'
ft.app(target=main)
