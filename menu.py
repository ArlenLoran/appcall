import flet
from flet import *
from functools import partial
import time
from controls import add_to_control_reference, return_control_reference
from screens import *
from configurations import *
import psutil

icon_color = passing_over_background

def closeapp(e):
    PROCNAME = "flet.exe"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()

def OpenOMS(e):
    ScreenFunctions.visible = False
    ScreenFunctions.update()
    ScreenCall.visible = False
    ScreenCall.update()
    ScreenCollaborators.visible = False
    ScreenCollaborators.update()
    ScreenSearch.visible = False
    ScreenSearch.update()
    ScreenOMS.visible = True
    ScreenOMS.update()
    textsfromicons(e)

def OpenSearch(e):
    ScreenOMS.visible = False
    ScreenOMS.update()
    ScreenFunctions.visible = False
    ScreenFunctions.update()
    ScreenCall.visible = False
    ScreenCall.update()
    ScreenCollaborators.visible = False
    ScreenCollaborators.update()
    ScreenSearch.visible = True
    ScreenSearch.update()
    textsfromicons(e)

def OpenFunctions(e):
    ScreenOMS.visible = False
    ScreenOMS.update()
    ScreenCall.visible = False
    ScreenCall.update()
    ScreenCollaborators.visible = False
    ScreenCollaborators.update()
    ScreenSearch.visible = False
    ScreenSearch.update()
    ScreenFunctions.visible = True
    ScreenFunctions.update()
    textsfromicons(e)

def OpenCollaborators(e):
    ScreenOMS.visible = False
    ScreenOMS.update()
    ScreenFunctions.visible = False
    ScreenFunctions.update()
    ScreenSearch.visible = False
    ScreenSearch.update()
    ScreenCall.visible = False
    ScreenCall.update()
    ScreenCollaborators.visible = True
    ScreenCollaborators.update()
    textsfromicons(e)

def OpenCall(e):
    ScreenOMS.visible = False
    ScreenOMS.update()
    ScreenFunctions.visible = False
    ScreenFunctions.update()
    ScreenSearch.visible = False
    ScreenSearch.update()
    ScreenCollaborators.visible = False
    ScreenCollaborators.update()
    ScreenCall.visible = True
    ScreenCall.update()
    textsfromicons(e)

def CloseAll(e):
    ScreenOMS.visible = False
    ScreenOMS.update()
    ScreenFunctions.visible = False
    ScreenFunctions.update()
    ScreenSearch.visible = False
    ScreenSearch.update()
    ScreenCollaborators.visible = False
    ScreenCollaborators.update()
    ScreenCall.visible = False
    ScreenCall.update()
    textsfromicons(e)

#Siderbar class
class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()

    def app_instance(self):
        add_to_control_reference("NavBar", self)

    def HighLight(self, e):
        if e.data == 'true':
            e.control.bgcolor = passing_over_background
            e.control.update()

            e.control.content.controls[0].icon_color = passing_over_icon
            e.control.content.controls[0].color = passing_over_icon
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()

            e.control.content.controls[0].icon_color = buttons_color
            e.control.content.controls[0].color = buttons_color
            e.control.content.update()



    def UserDate(self, initials:str, name:str, description:str):
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=40, height=40, bgcolor="white",
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials, size=16, weight='bold', color=buttons_color
                        )
                    ),
                    Column(
                        spacing=1,
                        alignment='center',
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                color=buttons_color,
                                weight='bold',
                                opacity=0,
                                text_align="right",
                                animate_opacity=200,

                            ),
                            Text(
                                description,
                                size=11,
                                color=buttons_color,
                                weight='w400',
                                opacity=0,
                                animate_opacity=200,

                            )
                        ]
                    )
                ]
            )
        )

    def ContainedIcon(self, icon_name:str, text:str, disable, bgcolor, iconcolor, function):
        return Container(
            width=180,
            height=45,
            on_click=function,
            border_radius=10,
            disabled=disable,
            on_hover=lambda e: self.HighLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        on_click=None,
                        bgcolor=bgcolor,
                        disabled=disable,
                        selected_icon_color=passing_over_icon,
                        icon_color=iconcolor,
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),

                            },
                            overlay_color={
                                "": "transparent"
                            },

                        )
                    ),
                    Text(
                        value=text,
                        color=iconcolor,
                        size=11,
                        opacity=1,
                        animate_opacity=200,

                    )
                ]
            ),
        )

    def build(self):
        self.app_instance()
        return Container(
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.UserDate("DHL", "Menu inicial", "Controle de presença"),
                    #Minimze and expand button
                    Container(
                        width=24,
                        height=24,
                        bgcolor=buttons_color,
                        border_radius=8,
                        on_click=partial(get_input2),

                    ),

                    Divider(height=5, color="transparent", ),
                    self.ContainedIcon(icons.SEARCH, "Consulta", False, icon_color, buttons_color, lambda e: OpenSearch(e)),
                    self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Chamada", False, None, buttons_color, lambda e: OpenCall(e)),
                    self.ContainedIcon(icons.PEOPLE_ROUNDED, "Colaboradores", False, None, buttons_color, lambda e: OpenCollaborators(e)),
                    self.ContainedIcon(icons.PIE_CHART_ROUNDED, "Funções", False, None, buttons_color, lambda e: OpenFunctions(e)),
                    self.ContainedIcon(icons.BAR_CHART, "OMS", False, None, buttons_color, lambda e: OpenOMS(e)),
                    self.ContainedIcon(icons.FAVORITE_ROUNDED, "Likes", True, None, "grey", lambda e: CloseAll(e)),
                    self.ContainedIcon(icons.WALLET_ROUNDED, "Wallet", True, None, "grey", lambda e: CloseAll(e)),
                    Divider(height=5, color=buttons_color),
                    self.ContainedIcon(icons.SETTINGS, "Settings", True, None, "grey", lambda e: CloseAll(e)),
                    self.ContainedIcon(icons.LOGOUT_ROUNDED, "Logout", False, None, buttons_color, lambda e: closeapp(e)),
                ]
            )
        )

control_map = return_control_reference()


def textsfromicons(e):
    iconselected = e.control.content.controls[0].icon
    for key, value in control_map.items():
        if key == 'NavBar':
            for texts in value.controls[0].content.controls[3:13]:
                if texts.height == 45:
                    if texts.content.controls[0].icon == iconselected:
                        texts.content.controls[0].bgcolor = icon_color
                        texts.content.controls[0].update()
                    else:
                        texts.content.controls[0].bgcolor = None
                        texts.content.controls[0].update()
            """value.controls[0].content.controls[0].content.controls[1].controls[0].visible = False
            value.controls[0].content.controls[0].content.controls[1].controls[1].visible = False
            value.controls[0].content.controls[0].content.controls[1].controls[0].update()
            value.controls[0].content.controls[0].content.controls[1].controls[1].update()"""


def get_input2(e):
    for key, value in control_map.items():
        if key == 'NavBar':
            if container_geral.width != 65:
                for user_input in value.controls[0].content.controls[0].content.controls[1].controls[:]:#value.controls[0].content.controls.value
                    user_input.opacity = 0
                    user_input.update()
                for user_input in value.controls[0].content.controls[3:10]: # loop pegando textos dos icones
                    user_input.content.controls[1].opacity = 0
                    user_input.content.controls[1].update()
                value.controls[0].content.controls[11].content.controls[1].opacity = 0
                value.controls[0].content.controls[11].content.controls[1].update()
                value.controls[0].content.controls[12].content.controls[1].opacity = 0
                value.controls[0].content.controls[12].content.controls[1].update()
                time.sleep(0.2)

                container_geral.width = 65
                container_geral.update()


            else:
                container_geral.width = 200
                container_geral.update()

                time.sleep(0.2)
                for user_input in value.controls[0].content.controls[0].content.controls[1].controls[:]:#value.controls[0].content.controls.value
                    user_input.opacity = 1
                    user_input.update()
                for user_input in value.controls[0].content.controls[3:10]:#loop pegando textos dos icones
                    user_input.content.controls[1].opacity = 1
                    user_input.content.controls[1].update()
                value.controls[0].content.controls[11].content.controls[1].opacity = 1
                value.controls[0].content.controls[11].content.controls[1].update()
                value.controls[0].content.controls[12].content.controls[1].opacity = 1
                value.controls[0].content.controls[12].content.controls[1].update()
            """TextTitle.opacity = 0
            TextDescription.opacity = 0
            TextTitle.update()
            TextDescription.opacity = 0"""



            """for user_input in value.controls[0].content.controls[3:10]: # loop pegando icones
                print(user_input.content.controls[0].icon)"""

            """print(value.controls[0]) # Container onde está tudo dentro
            print(value.controls[0].content.controls[3:]) # Container onde está icon e texto
            print(value.controls[0].content.controls[1]) # Quadradinho que clica para abrir e fechar menu
            print(value.controls[0].content.controls[3].content.controls[0]) # Container do icon
            print(value.controls[0].content.controls[3].content.controls[1]) # Container texto"""


container_geral = Container(
            expand=True,
            width=65,
            border=border.all(2, background_color),
            bgcolor="white",
            border_radius=10,
            animate=animation.Animation(500, 'decelerate'),
            alignment=alignment.top_center, #center
            padding=10,
            content=ModernNavBar(),

        )




