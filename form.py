from flet import *
from controls import add_to_control_reference
from buttons import return_form_button
import sqlite3
from database import *
from TablesLines import RunAndFilterQuery, detailscancel, add, update, RunAndFilterQueryCall, RunAndFilterSearch, filterssearch, detailsfunctionscancel, addfunctions, updatefunctions, RunAndFilterQueryOMS, DetailsOMSCancel
from configurations import *
from dateinput import date as datecall
from dateinput2 import date as datecall2
from dateinput3 import date as datecall3
from dateinput4 import date as datecall4
from dateinput5 import date as datecall5

class AppForm(UserControl):
        def __int__(self):
            super().__int__()

        def app_form_input_instance(self):
            add_to_control_reference("AppForm", self)

        def app_form_input_field(self, sugestion, name: str, expand: int, visible):
            return Container(
                expand=True,
                height=45,
                visible=visible,
                bgcolor="#ebebeb",
                border_radius=6,
                padding=8,
                content=Column(
                    expand=True,
                    spacing=1,
                    controls=[
                        Text(
                            value=name,
                            size=9, color="black",
                            weight="bold"
                        ),
                        TextField(
                            border_color="transparent",
                            height=20,
                            text_size=13,
                            hint_text=sugestion,
                            hint_style=TextStyle(size=12, color="grey"),
                            content_padding=0,
                            cursor_color="black",
                            cursor_width=1,
                            cursor_height=18,
                            color="black"
                        ),
                    ]
                )
            )

        def Dropdown(self, sugestion, name, values):
            listaFunc = []
            for x in values:
                listaFunc.append(x)

            return Container(
                height=45,
                bgcolor="#ebebeb",
                border_radius=6,
                expand=1,
                padding=8,
                content=Column(
                    expand=True,
                    spacing=1,
                    controls=[
                            Text(
                                value=name,
                                size=9, color="black",
                                weight="bold"
                            ),
                        Dropdown(
                            border_color="transparent",
                            height=20,
                            text_size=13,
                            hint_text=sugestion,
                            hint_style=TextStyle(size=12, color="grey"),
                            options=[dropdown.Option(x) for x in listaFunc],
                            content_padding=0,
                            color="black",
                        )
                        ,
                    ]
                )
            )

        def DropdownQuery(self, sugestion,  name, query):
            listaFunc = []

            lt = SQLCodeSearch(query)
            for tabela in lt:
                result = ("%s" % (tabela))
                listaFunc.append(result)

            return Container(
                height=45,
                bgcolor="#ebebeb",
                border_radius=6,
                expand=1,
                padding=8,
                content=Column(
                    expand=True,
                    spacing=1,
                    controls=[
                            Text(
                                value=name,
                                size=9, color="black",
                                weight="bold"
                            ),
                        Dropdown(
                            border_color="transparent",
                            height=20,
                            text_size=13,
                            options=[dropdown.Option(x) for x in listaFunc],
                            content_padding=0,
                            hint_text=sugestion,
                            hint_style=TextStyle(size=12, color="grey"),
                            color="black",
                        )
                        ,
                    ]
                )
            )

        def FilterCoord(self):
            list = []
            users = SQLCodeSearch(f"""SELECT DISTINCT funcao, nivel FROM Funcoes""")
            if not users == "":
                keys = ['funcao', 'nivel']
                result = [dict(zip(keys, values)) for values in users]
                for x in result:
                    nivel = x['nivel']
                    if nivel == "LIDERANÇA":
                        conn = Connection()
                        cur = conn.cursor()
                        # fetch all the data and store it in a variable
                        lp = SQLCodeSearch(f"""SELECT DISTINCT nome FROM Colaboradores WHERE funcao = '{x['funcao']}'""")
                        for tabela in lp:
                            result = ("%s" % (tabela))
                            list.append(result)

            return Container(
                height=45,
                bgcolor="#ebebeb",
                border_radius=6,
                expand=1,
                padding=8,
                content=Column(
                    expand=True,
                    spacing=1,
                    controls=[
                        Text(
                            value="Gestor responsável",
                            size=9, color="black",
                            weight="bold"
                        ),
                        Dropdown(
                            border_color="transparent",
                            height=20,
                            text_size=13,
                            options=[dropdown.Option(x) for x in list],
                            content_padding=0,
                            color="black",
                        )
                    ]
                )
            )

        def build(self):
            self.app_form_input_instance()
            return Container(
                expand=True,
                bgcolor="white10",
                border=border.all(2, "#ebebeb"),
                border_radius=8,
                padding=15,
                content=Column(
                    expand=True,
                    controls=[
                        Row(
                            controls=[
                                Text("Cadastrar novo colaborador", color="black"),
                            ],
                        ),
                        Row(
                            controls=[
                                self.app_form_input_field(None, "Matrícula", 1, True),
                                self.app_form_input_field(None, "Nome", 3, True),
                                self.DropdownQuery(None, "Função", f"SELECT DISTINCT funcao FROM Funcoes"),
                            ],
                        ),
                                Row(
                                    controls=[
                                        self.FilterCoord(),
                                        self.Dropdown(None, "Turno", ["1° TURNO", "2° TURNO", "3° TURNO", "ADM"]),
                                        self.Dropdown(None, "Área", ["WAREHOUSE", "EMBELLISHMENT", "ADM"]),
                                        self.app_form_input_field(None, "E-mail", 1, True),
                                        self.app_form_input_field(None, "ID", 1, False),

                                    ],
                                ),
                                Divider(height=2, color="transparent"),
                                Row(
                                    alignment=MainAxisAlignment.END,
                                    controls=[
                                        return_form_button(lambda e: detailscancel(e), buttons_color, icons.CLOSE, "Cancelar edição", False),
                                        return_form_button(lambda e: update(e), "green", icons.DONE, "Salvar edição", False),
                                        return_form_button(lambda e: add(e), buttons_color, icons.ADD_ROUNDED, "Adicionar colaborador", True)
                                    ]
                                )


                            ]
                        ),


                )


class AppFormCall(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("AppFormCall", self)

    def app_form_input_field(self, sugestion, name: str, expand: int, visible):
        return Container(
            expand=True,
            height=45,
            visible=visible,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Stack(
                        controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        hint_text=sugestion,
                        read_only=True,
                        hint_style=TextStyle(size=12, color="grey"),
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black"
                    )]),
                ]
            )
        )

    def Dropdown(self, sugestion, name, values):
        listaFunc = []
        for x in values:
            listaFunc.append(x)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        options=[dropdown.Option(x) for x in listaFunc],
                        content_padding=0,
                        color="black",
                    )
                    ,
                ]
            )
        )

    def DropdownQuery(self, sugestion, name, query):
        listaFunc = []

        lt = SQLCodeSearch(query)
        for tabela in lt:
            result = ("%s" % (tabela))
            listaFunc.append(result)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        on_change=lambda e: RunAndFilterQueryCall(e),
                        options=[dropdown.Option(x) for x in listaFunc],
                        content_padding=0,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        color="black",
                    )
                    ,
                ]
            )
        )

    def FilterCoord(self):
        list = []
        users = SQLCodeSearch(f"""SELECT DISTINCT funcao, nivel FROM Funcoes""")
        if not users == "":
            keys = ['funcao', 'nivel']
            result = [dict(zip(keys, values)) for values in users]
            for x in result:
                nivel = x['nivel']
                if nivel == "LIDERANÇA":
                    conn = Connection()
                    cur = conn.cursor()
                    # fetch all the data and store it in a variable
                    lp = SQLCodeSearch(f"""SELECT DISTINCT nome FROM Colaboradores WHERE funcao = '{x['funcao']}'""")
                    for tabela in lp:
                        result = ("%s" % (tabela))
                        list.append(result)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value="Gestor responsável",
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        on_change=lambda e: RunAndFilterQueryCall(e),
                        options=[dropdown.Option(x) for x in list],
                        content_padding=0,
                        color="black",
                    )
                ]
            )
        )

    def build(self):
        self.app_form_input_instance()
        return Container(
            expand=True,
            bgcolor="white10",
            border=border.all(2, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            Text("Realizar chamada", color="black"),
                        ],
                    ),
                    Row(
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            datecall,
                            self.FilterCoord(),
                            self.app_form_input_field(None, "ID", 1, False),
                        ],
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[

                        ]
                    )

                ]
            ),

        )

class AppFormSearch(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("AppFormSearch", self)

    def app_form_input_field(self, sugestion, name: str, expand: int, visible):
        return Container(
            expand=True,
            height=45,
            visible=visible,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Stack(
                        controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        hint_text=sugestion,
                        read_only=True,
                        hint_style=TextStyle(size=12, color="grey"),
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black"
                    )]),
                ]
            )
        )

    def Dropdown(self, sugestion, name, values, default):
        listaFunc = []
        for x in values:
            listaFunc.append(x)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        value=default,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        options=[dropdown.Option(x) for x in listaFunc],
                        content_padding=0,
                        color="black",
                    )
                    ,
                ]
            )
        )

    def DropdownQuery(self, sugestion, name, query):
        listaFunc = []

        lt = SQLCodeSearch(query)
        for tabela in lt:
            result = ("%s" % (tabela))
            listaFunc.append(result)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        on_change=lambda e: RunAndFilterQueryCall(e),
                        options=[dropdown.Option(x) for x in listaFunc],
                        content_padding=0,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        color="black",
                    )
                    ,
                ]
            )
        )

    def build(self):
        self.app_form_input_instance()
        return Container(
            expand=True,
            bgcolor="white10",
            border=border.all(2, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            Text("Consulta", color="black"),
                        ],
                    ),
                    Row(
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            datecall2,
                            datecall3,
                            self.Dropdown(None, "Status", ["TODOS", "PRESENTE", "AUSENTE"], "TODOS"),
                        ],
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_form_button(lambda e: RunAndFilterSearch(e), buttons_color, icons.SEARCH,
                                               "Pesquisar", True)
                        ]
                    )

                ]
            ),

        )

class AppFormFunctions(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("AppFormFunctions", self)

    def app_form_input_field(self, sugestion, name: str, expand: int, visible):
        return Container(
            expand=True,
            height=45,
            visible=visible,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black"
                    ),
                ]
            )
        )

    def Dropdown(self, sugestion, name, values):
        listaFunc = []
        for x in values:
            listaFunc.append(x)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        options=[dropdown.Option(x) for x in listaFunc],
                        content_padding=0,
                        color="black",
                    )
                    ,
                ]
            )
        )

    def DropdownQuery(self, sugestion, name, query):
        listaFunc = []

        lt = SQLCodeSearch(query)
        for tabela in lt:
            result = ("%s" % (tabela))
            listaFunc.append(result)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        on_change=lambda e: RunAndFilterQueryCall(e),
                        options=[dropdown.Option(x) for x in listaFunc],
                        content_padding=0,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        color="black",
                    )
                    ,
                ]
            )
        )

    def build(self):
        self.app_form_input_instance()
        return Container(
            expand=True,
            bgcolor="white10",
            border=border.all(2, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            Text("Gerenciamento de funções", color="black"),
                        ],
                    ),
                    Row(
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            self.app_form_input_field(None, "Função", 1, True),
                            self.Dropdown(None, "Nível", ["COLABORADOR", "LIDERANÇA"]),
                            self.app_form_input_field(None, "ID", 1, False),
                        ],
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_form_button(lambda e: detailsfunctionscancel(e), buttons_color, icons.CLOSE,
                                               "Cancelar edição", False),
                            return_form_button(lambda e: updatefunctions(e), "green", icons.DONE, "Salvar edição", False),
                            return_form_button(lambda e: addfunctions(e), buttons_color, icons.ADD_ROUNDED,
                                               "Adicionar função", True)
                        ]
                    )

                ]
            ),

        )

class AppFormOMS(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("AppFormOMS", self)

    def app_form_input_field(self, sugestion, name: str, expand: int, visible):
        return Container(
            expand=True,
            height=45,
            visible=visible,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black"
                    ),
                ]
            )
        )

    def Dropdown(self, sugestion, name, values, default):
        listaFunc = []
        for x in values:
            listaFunc.append(x)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        value=default,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        options=[dropdown.Option(x) for x in listaFunc],
                        content_padding=0,
                        color="black",
                    )
                    ,
                ]
            )
        )

    def DropdownQuery(self, sugestion, name, query):
        listaFunc = []

        lt = SQLCodeSearch(query)
        for tabela in lt:
            result = ("%s" % (tabela))
            listaFunc.append(result)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        value="TODOS",
                        on_change=lambda e: RunAndFilterQueryCall(e),
                        options=[dropdown.Option(x.upper()) for x in listaFunc],
                        content_padding=0,
                        hint_text=sugestion,
                        hint_style=TextStyle(size=12, color="grey"),
                        color="black",
                    )
                    ,
                ]
            )
        )

    def FilterCoord(self):
        list = ['TODOS']
        users = SQLCodeSearch(f"""SELECT DISTINCT funcao, nivel FROM Funcoes""")
        if not users == "":
            keys = ['funcao', 'nivel']
            result = [dict(zip(keys, values)) for values in users]
            for x in result:
                nivel = x['nivel']
                if nivel == "LIDERANÇA":
                    conn = Connection()
                    cur = conn.cursor()
                    # fetch all the data and store it in a variable
                    lp = SQLCodeSearch(f"""SELECT DISTINCT nome FROM Colaboradores WHERE funcao = '{x['funcao']}'""")
                    for tabela in lp:
                        result = ("%s" % (tabela))
                        list.append(result)

        return Container(
            height=45,
            bgcolor="#ebebeb",
            border_radius=6,
            expand=1,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value="Gestor responsável",
                        size=9, color="black",
                        weight="bold"
                    ),
                    Dropdown(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        on_change=lambda e: RunAndFilterQueryCall(e),
                        value='TODOS',
                        options=[dropdown.Option(x) for x in list],
                        content_padding=0,
                        color="black",
                    )
                ]
            )
        )


    def build(self):
        self.app_form_input_instance()
        return Container(
            expand=True,
            bgcolor="white10",
            border=border.all(2, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            Text("Informações detalhadas", color="black"),
                        ],
                    ),
                    Row(
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            datecall4,
                            datecall5,
                            self.Dropdown(None, "Turno", ["1° TURNO", "2° TURNO", "3° TURNO", "ADM", "TODOS"], "TODOS"),
                        ],
                    ),
                    Row(
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            self.Dropdown(None, "Área", ["WAREHOUSE", "EMBELLISHMENT", "ADM", "TODAS"], "TODAS"),
                            self.FilterCoord(),
                        ],
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_form_button(lambda e: DetailsOMSCancel(e), buttons_color, icons.CLOSE,
                                               "Cancelar visualização", False),
                            return_form_button(lambda e: RunAndFilterQueryOMS(e), buttons_color, icons.SEARCH_ROUNDED,
                                               "Consultar", True)
                        ]
                    )

                ]
            ),

        )

class AppFormOMSInfos(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("AppFormOMSInfos", self)

    def app_form_input_field(self, sugestion, name: str, expand: int, visible, cortitle):
        return Container(
            expand=True,
            height=45,
            visible=visible,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                expand=True,
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9, color=cortitle,
                        weight="bold"
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=13,
                        hint_text=sugestion,
                        read_only=True,
                        hint_style=TextStyle(size=12, color="grey"),
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black"
                    ),
                ]
            )
        )

    def build(self):
        self.app_form_input_instance()
        return Container(
                expand=True,
                bgcolor="white10",
                visible=False,
                border=border.all(1, "#ebebeb"),
                border_radius=8,
                padding=15,
                content=Column(
                    expand=True,
                    controls=[
                    Column([
                        Text("Visualizando detalhes", color=buttons_color),
                        Row([
                            self.app_form_input_field(None, "Exame", 1, True, "green"),
                            self.app_form_input_field(None, "Suspenso", 1, True, "red"),
                            self.app_form_input_field(None, "Falecimento F.", 1, True, "red"),
                            self.app_form_input_field(None, "Férias", 1, True, "green"),
                            self.app_form_input_field(None, "Atestado", 1, True, "red"),
                            self.app_form_input_field(None, "Falta", 1, True, "red"),
                            self.app_form_input_field(None, "Treinamento", 1, True, "green"),
                        ]),
                        Row([
                            self.app_form_input_field(None, "Desligado", 1, True, "green"),
                            self.app_form_input_field(None, "Sinergia", 1, True, "green"),
                            self.app_form_input_field(None, "Licença", 1, True, "green"),
                            self.app_form_input_field(None, "Afastado", 1, True, "green"),
                            self.app_form_input_field(None, "Covid", 1, True, "red"),
                            self.app_form_input_field(None, "Transferido", 1, True, "green"),
                            self.app_form_input_field(None, "Folga", 1, True, "green"),
                        ]),
                        Row([
                            self.app_form_input_field(None, "Declaração", 1, True, "red"),
                            self.app_form_input_field(None, "***", 1, True, "grey"),
                            self.app_form_input_field(None, "***", 1, True, "grey"),
                            self.app_form_input_field(None, "***", 1, True, "grey"),
                            self.app_form_input_field(None, "***", 1, True, "grey"),
                            self.app_form_input_field(None, "***", 1, True, "grey"),
                            self.app_form_input_field(None, "***", 1, True, "grey"),
                        ]),


                    ], )


                    ]
                ),

            )