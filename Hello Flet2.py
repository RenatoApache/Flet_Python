import flet as ft
import time

def main(page: ft.Page):
    t = ft.Text()
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(100):
        t.value = f"Step {i}"
        page.update()
        time.sleep(0.1)

app = ft.app(target=main)
app.run()


