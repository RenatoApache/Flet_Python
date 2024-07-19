import os
from flet import *

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: Page):
    gv = GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(1000):
        gv.controls.append(
            Container(
                Text(f"Item {i}", size=80, color="#001188"),
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(2,colors.AMBER_500),
                border_radius=border_radius.all(8)
            )
        )
    page.update()

app(target=main, view=WEB_BROWSER)