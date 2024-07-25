'''criando um projeto de lista de tarefas usando flet'''
import flet
from flet import *



#Funcção principal da aplicação
def main(page:Page):
    page.title="Tarefas"
    page.horizontal_alignment="center"
    page.scroll="adaptative"
    page.update()
    
    pass

flet.app(target=main)