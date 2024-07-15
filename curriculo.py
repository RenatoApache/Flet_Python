import flet as ft

nome = ft.TextField(label="Nome completo")
email = ft.TextField(label="E-mail")
experiencia = ft.TextField(label="Experiência profissional", multiline=True)

page = ft.Page()
page.add(nome, email, experiencia)

def gerar_pagina():
    # Aqui você pode processar os dados inseridos e gerar a nova página
    # Por exemplo, criar um PDF com as informações do currículo
    # ou exibir os dados em uma nova tela.
    # Lembre-se de adaptar essa parte conforme suas necessidades.
    nova_pagina = ft.Page()
    # Adicione os elementos à nova página conforme necessário.
    # Exemplo:
    nova_pagina.add(ft.Text("Currículo gerado com sucesso!"))
    return nova_pagina

ft.app(target=gerar_pagina)