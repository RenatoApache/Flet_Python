'''criando um projeto de lista de tarefas usando flet'''
import flet
from flet import *

#Classe de tarefa
class Task(UserControl):
    def __init__(self, task_name, tasl_status_change, task_delete):
        super().__init__()
        self,completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

#Classe da aplicação toda
class TodoApp(UserControl):
    def build(self):
        self.new_task = TextField(
            hint_text="Escreva a tarefa para adicionar!",
            expand=True
        )
        self.task = Column()

        self.filter = Tabs(
            selected_index = 0,
            on_change = self.tabs_changed,
            tabs = [Tab(text="Todas tarefas"), Tab(text="Tarefas ativas"), Tab(text="Tarefas concluidas"),]
        )

        return Column(
            width=600,
            controls=[
                Row([Text(value="Tarefas", style="headlineMedium")])
            ]
        )

    def add_clicked(self):
        pass
                 
#Funcção principal da aplicação
def main(page:Page):
    page.title="Tarefas"
    page.horizontal_alignment="center"
    page.scroll="adaptative"
    page.update()
    
    app = TodoApp()

    page.add(app)

flet.app(target=main)