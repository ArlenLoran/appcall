from flet import *
from controls import return_control_reference
from form_helper import Formhelper
import sqlite3
from database import *
from configurations import *
from TablesLines import *

control_map = return_control_reference()



def update_text(e):
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

def get_input(e):
    for key, value in control_map.items():
        if key == 'AppForm':
            data = DataRow(cells=[])
            #Alterando o titulo do forms
            value.controls[0].content.controls[0].controls[0].value = "Alterei o titulo da pagina"
            # percorrendo a linha 4 do forms OBS: Começa em 0
            for user_input in value.controls[0].content.controls[3].controls[:]:
                #Alterando Titulo do input
                if user_input.content.controls[0].value == "Consegu":
                    user_input.content.controls[0].value = "Consegui"
                    user_input.content.controls[0].update()
                #Alterando Valor do input
                if user_input.content.controls[0].value == "Consegui":
                    user_input.content.controls[1].value = "Consegui"
                    user_input.content.controls[1].update()
                #Alterando cor de fundo do input
                if user_input.content.controls[0].value == "Consegui":
                    user_input.bgcolor = "green"
                    user_input.update()
                #Alterando cor de fundo do form onde estão os inputs
                if user_input.content.controls[0].value == "Consegui":
                    value.controls[0].bgcolor = "blue"
                    value.controls[0].update()

        if key == "AppDataTable":
            pass


def get_input2(e):
    for key, value in control_map.items():
        if key == 'AppForm':
            #Primeira linha percorre a segunda linha do form, a segunda verifica o titulo do form e a ultima muda o background do form cujo titulo informado
            for user_input in value.controls[0].content.controls[2].controls[:]:
                if user_input.content.controls[0].value == "Field Two":
                    user_input.bgcolor = "green"
                    user_input.update()
            #`Primeira verifica o titulo do form e a segunda linha altera o valor do form para o valor desejado
                if user_input.content.controls[0].value == "Field Two":
                    user_input.content.controls[1].value = "Alterado"
                    user_input.content.controls[1].update()

def get_input3(e):
    for key, value in control_map.items():
        if key == 'AppForm':
            print(value)
            value.controls[0].bgcolor = "blue"
            value.controls[0].update()
            print(value.controls[0]) #Primeiro container
            print(value.controls[0].content) #Primeiro content
            print(value.controls[0].content.controls[0]) #Primeira linha
            print(value.controls[0].content.controls[1]) #Segunda linha
            print(value.controls[0].content.controls[0].controls[0]) #Texto que está na primeira linha
            print(value.controls[0].content.controls[1].controls[0]) #input segunda linha
            print(value.controls[0].content.controls[2].controls[1]) #Segundo input terceira linha
            print(value.controls[0].content.controls[2].controls[1].content) #content do segundo input terceira linha do forms
            print(value.controls[0].content.controls[2].controls[1].content.controls[0]) #Titulo do segundo input terceira linha do forms
            print(value.controls[0].content.controls[2].controls[1].content.controls[1]) #Acessando entrada de texto do segundo input terceira linha do forms
            value.controls[0].content.controls[2].controls[4].content.controls[1].value = "OPERADOR DE EMPILHADEIRA" #Alterando valor do dropdown na terceira linha do forms input 5
            value.controls[0].content.controls[2].controls[4].content.controls[1].update()
            value.controls[0].content.controls[2].controls[0].bgcolor = "red"
            value.controls[0].content.controls[2].controls[0].update()
            print(value.controls[0].content.controls[2].controls[4].content.controls[1].value)


            """value.controls[0].content.controls[0].controls[0].value = "Alterei o titulo da pagina"
            value.controls[0].content.controls[0].controls[0].update()
            #Pegando titulos dos inputs
            print(value.controls[0].content.controls[1].controls[0].content.controls[0]) # Primeiro field linha 1
            print(value.controls[0].content.controls[2].controls[0].content.controls[0]) # Primeiro Field linha 2
            print(value.controls[0].content.controls[2].controls[1].content.controls[0])  # Segundo Field linha 2
            print(value.controls[0].content.controls[2].controls[1].content.controls[0])  # Segundo Field linha 2
            #Pegando valores dos inputs
            print(value.controls[0].content.controls[1].controls[0].content.controls[1])  # Primeiro field linha 1
            print(value.controls[0].content.controls[1].controls[0].content.controls[1].value)
            print(value.controls[0].content.controls[2].controls[1].content.controls[1].value)"""

            #Primeira linha percorre a segunda linha do form, a segunda verifica o titulo do form e a ultima muda o background do form cujo titulo informado
            for user_input in value.controls[0].content.controls[2].controls[:]:
                if user_input.content.controls[0].value == "Teste query":
                    user_input.content.controls[1].value = "OPERADOR DE EMPILHADEIRA"
                    user_input.content.controls[1].update()
                if user_input.content.controls[0].value == "Teste lista":
                    user_input.content.controls[1].value = "2"
                    user_input.content.controls[1].update()









def return_form_button(function, color, icon, text, visible):
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=function,
            visible=visible,
            bgcolor=color,
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icon,
                        size=12,
                    ),
                    Text(
                        text,
                        size=11,
                        weight="bold"
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6)
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        )
    )










