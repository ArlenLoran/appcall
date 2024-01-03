import flet
from flet import *
from configurations import *
from screens import *
from menu import container_geral
from TablesLines import RunAndFilterQuery, RunAndFilterSearch, RunAndFilterQueryFunctions

def main(page: Page):
    page.title = 'Controle de presença'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    page.add(

        Container(
            # width=1100,
            # height=520,
            expand=True,
            bgcolor="white",
            border_radius=10,
            animate=animation.Animation(500, 'decelerate'),
            alignment=alignment.top_center,
            padding=10,
            content=Row([
                Column(
                    alignment=alignment.top_center,
                    horizontal_alignment=CrossAxisAlignment.START,
                    controls=[container_geral]),
                    ScreenCollaborators, ScreenCall, ScreenSearch, ScreenFunctions, ScreenOMS

            ],)

        ),

    )

    page.update()
    RunAndFilterQuery(page)
    RunAndFilterSearch(page)
    RunAndFilterQueryFunctions(page)

if __name__ == '__main__':
    flet.app(target=main)