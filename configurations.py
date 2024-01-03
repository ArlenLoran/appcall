from flet import *
import os
from database import *
import pandas as pd
import datetime

buttons_color = "#D40511" #081d33
background_color = "#ebebeb"
layout_color = "#23262a"
white_color = "white"
buttons_color_less = "#0A2440" #0A2440
passing_over_background = "#FFEFF0"
passing_over_icon = "red"


def change_date(e):
    print(f"Date picker changed, value is {date_picker.value}")


def date_picker_dismissed(e):
    print(f"Date picker dismissed, value is {date_picker.value}")

date_picker = DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),
    )

def open_fileOMS(e):
    os.startfile('RelatorioOMS.xlsx')
    close_banner(e)

def open_fileCall(e):
    os.startfile('RelatorioChamada.xlsx')
    close_banner(e)

def open_fileCollaborators(e):
    os.startfile('Colaboradores.xlsx')
    close_banner(e)

def close_banner(e):
    e.page.banner.open = False
    e.page.update()



def open_banner_error(mensa, e):
    e.page.banner = Banner(
        bgcolor=buttons_color,
        leading=Icon(icons.ERROR_OUTLINE_ROUNDED, color="white", size=30),
        content=Text(
            mensa, color="white"
        ),
        actions=[
            TextButton("OK", on_click=close_banner, style=ButtonStyle(color="white"))
        ]
    )
    e.page.banner.open = True
    e.page.update()

def open_banner_sucess(mensa, e):
    e.page.banner = Banner(
        bgcolor=buttons_color,
        leading=Icon(icons.CHECK_CIRCLE_OUTLINE_ROUNDED, color="white", size=30),
        content=Text(
                mensa, color="white"
            ),
            actions=[
                TextButton("OK", on_click=close_banner, style=ButtonStyle(color="white"))
            ]
        )
    e.page.banner.open = True
    e.page.update()

def open_banner_downloadOMS(mensa, e):
    e.page.banner = Banner(
            bgcolor=buttons_color,
            leading=Icon(icons.CHECK_CIRCLE_OUTLINE_ROUNDED, color="white", size=30),
            content=Text(
                mensa, color="white"
            ),
            actions=[
                TextButton("Abrir", on_click=open_fileOMS, style=ButtonStyle(color="white")),
                TextButton("Ok", on_click=close_banner, style=ButtonStyle(color="white"))
            ]
        )
    e.page.banner.open = True
    e.page.update()

def open_banner_downloadCall(mensa, e):
    e.page.banner = Banner(
            bgcolor=buttons_color,
            leading=Icon(icons.CHECK_CIRCLE_OUTLINE_ROUNDED, color="white", size=30),
            content=Text(
                mensa, color="white"
            ),
            actions=[
                TextButton("Abrir", on_click=open_fileCall, style=ButtonStyle(color="white")),
                TextButton("Ok", on_click=close_banner, style=ButtonStyle(color="white"))
            ]
        )
    e.page.banner.open = True
    e.page.update()

def open_banner_downloadCollaborators(mensa, e):
    e.page.banner = Banner(
            bgcolor=buttons_color,
            leading=Icon(icons.CHECK_CIRCLE_OUTLINE_ROUNDED, color="white", size=30),
            content=Text(
                mensa, color="white"
            ),
            actions=[
                TextButton("Abrir", on_click=open_fileCollaborators, style=ButtonStyle(color="white")),
                TextButton("Ok", on_click=close_banner, style=ButtonStyle(color="white"))
            ]
        )
    e.page.banner.open = True
    e.page.update()


def open_banner_delete(mensa, function, e):
    e.page.banner = Banner(
            bgcolor=buttons_color,
            leading=Icon(icons.CHECK_CIRCLE_OUTLINE_ROUNDED, color="white", size=30),
            content=Text(
                f"{mensa}", color="white"
            ),
            actions=[
                TextButton("Excluir", on_click=function, style=ButtonStyle(color="white")),
                TextButton("Cancelar", on_click=close_banner, style=ButtonStyle(color="white"))
            ]
        )
    e.page.banner.open = True
    e.page.update()

def ExportToExcel(e):
    users = SQLCodeSearch(f"""SELECT * FROM Colaboradores""")
    keys = ['id', 'matricula', 'nome', 'funcao', 'gestor', 'turno', 'email', 'setor']
    if not users == []:
        result = [dict(zip(keys, values)) for values in users]
        data = {'ID': [], 'MATRICULA': [], 'NOME': [], 'FUNÇÃO': [], 'GESTOR': [], 'TURNO': [], 'E-MAIL': []}
        for x in result:
            data['ID'].append(x['id']),
            data['MATRICULA'].append(x['matricula']),
            data['NOME'].append(x['nome']),
            data['FUNÇÃO'].append(x['funcao']),
            data['GESTOR'].append(x['gestor']),
            data['TURNO'].append(x['turno']),
            data['E-MAIL'].append(x['email']),
        df = pd.DataFrame(data)
        df.to_excel("Colaboradores.xlsx", index=False)
        open_banner_sucess("Download realizado com sucesso", e)
    else:
        pass



