'''criando um projeto de lista de tarefas usando flet'''
import flet
from flet import *

#Classe de tarefa
class Task(UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self,completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        self.display_task = Checkbox(
            value = False, label=self.task_name, on_change=self.task_status_change
        )

        self.edit_name = TextField(expand=1) #Entrada de texto da edição tarefa

        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment = "center",
            controls = [
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Editar tarefa", #Texto de orientação
                            on_click=self.edit_clicked,
                            icon_color=colors.GREEN,
                        ),
                        IconButton(
                            icon=icons.Delete_OUTLINED,
                            tooltip="Deletar tarefa", #Texto de orientação
                            on_click=self.delete_clicked,
                            icon_color=colors.RED,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment = "center",
            controls=[
                IconButton(
                    icons=icons.DENE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    Tooltip="Atualizar tarefa",
                    on_click=self.save_clicked,
                )
            ]
        )
        return Column(controls=[self.display_view, self.edit_view])
    
    def edit_clicked(self, e):
        self.edit_name.values=self.display_task.label
        self.display_view.visible=False
        self.edit_name.visible = True
        self.update()

    def save_clicked(self):
        self.display_task.label=self.edit_name.value
        self.display_view.visible=True
        self.edit_view.visible=False
        self.update()

    def delete_clicked(self):
        self.task_delete(self)

    def status_change(self):
        self.completed=self.display_task.values()
        self.task_status_change(self)

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
                #Titulo da aplicação
                Row([Text(value="Tarefas", style="headlineMedium")], alignment="center"),
                Row(controls = [self.new_task, FloatingActionButton(icon=icons.ADD, on_click = self.add_clicked),],),
                Column(
                    spacing=20,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Limpar as tarefas completadas".upper(),
                                    on_click=self.clear_clicked,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    def add_clicked(self, e):
        if self.new_task.value:
            task=Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value=""
            self.new.task.focus()
            self.update()

    def task_status_change(self, task):
        pass

    def task_delete(self, task):
        pass

    def tab_changed(self, e):
        pass
    
    def clear_clicked(self, e):
        pass

    def update(self):
        status=self.filter.tabs[self.filter.selected_index].text
        count=0
        for task in self.task.controls:
            status=="Todas tarefas"
            or (status=="tarefae ativas" and task.completed)
                 
#Funcção principal da aplicação
def main(page:Page):
    page.title="Tarefas"
    page.horizontal_alignment="center"
    page.scroll="adaptative"
    page.update()
    
    app = TodoApp()

    page.add(app)

flet.app(target=main)