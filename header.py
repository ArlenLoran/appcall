from flet import *
from controls import add_to_control_reference, return_control_reference
from configurations import *


control_map = return_control_reference()

class AppHeader(UserControl):
    def __int__(self):
        super().__int__()

    def app_header_instance(self):
        add_to_control_reference("AppHeader", self)

    def app_header_brand(self):
        return Container(
            content=Text(
                "Gerenciamento de usuários",
                size=15,
                color="white"

            )
        )

    def app_hearder_search(self):
        return Container(
            width=320,
            height=40,
            bgcolor="white10",
            border_radius=6,
            padding=8,
            opacity=0,
            animate_opacity=320,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(""),
                    Icon(name=icons.SEARCH_ROUNDED, size=25, opacity=0.85, color="white"),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        text_style=TextStyle(color="white"),
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                        hint_text="Search",
                        hint_style=TextStyle(color="grey"),
                        on_change=lambda e: self.filter_data_table(e),


                    )

                ]
            )
        )

    def app_item_avatar(self):
        return Container(content=IconButton(icons.EXIT_TO_APP, icon_color="white", icon_size=30))

    def show_search_bar(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
        else:
            self.controls[0].content.controls[1].content.controls[1].value = ""
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].update()

    def filter_data_table(self, e):
        for key, value in control_map.items():
            if key == "AppDataTable":
                if len(value.controls[0].controls[0].rows) != 0:
                    for data in value.controls[0].controls[0].rows[:]:
                        if e.data.lower() in data.cells[0].content.controls[0].value.lower():
                            data.visible = True
                            data.update()
                        else:
                            data.visible = False
                            data.update()
        print(e.data)

    def build(self):
        self.app_header_instance()


        return Container(
            expand=True,
            on_hover=None,
            height=60,
            bgcolor=buttons_color,
            border_radius=border_radius.only(top_left=15, top_right=15),
            padding=padding.only(left=15, right=15),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.app_header_brand(),
                    Text("Deutsche Post DHL Group", weight="bold", size=15, color="white"),
                    #self.app_item_avatar(),
                ]
            )

        )



