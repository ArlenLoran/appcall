from flet import *
from configurations import *
from database import *
from controls import return_control_reference, add_to_control_reference
from dateinput import View_date as datecall
from dateinput2 import View_date as datecall2
from dateinput3 import View_date as datecall3
from dateinput4 import View_date as datecall4
from dateinput5 import View_date as datecall5
from queriesoms import *

buttons_color = "#D40511" #081d33

control_map = return_control_reference()

def detailsfunctions(e):
    for key, value in control_map.items():
        if key == 'AppFormFunctions':
            value.controls[0].content.controls[3].controls[0].content.visible = True
            value.controls[0].content.controls[3].controls[0].content.update()
            value.controls[0].content.controls[3].controls[1].content.visible = True
            value.controls[0].content.controls[3].controls[1].content.update()
            value.controls[0].content.controls[3].controls[2].content.disabled = True
            value.controls[0].content.controls[3].controls[2].content.update()
            value.controls[0].content.controls[0].controls[
                0].value = f"Editando informações da função {e.control.data.controls[1].value}"
            value.controls[0].content.controls[0].controls[0].color = "red"
            value.controls[0].content.controls[0].controls[0].update()
            value.controls[0].content.controls[1].controls[2].content.controls[1].value = e.control.data.controls[0].value
            value.controls[0].content.controls[1].controls[0].content.controls[1].value = e.control.data.controls[1].value
            value.controls[0].content.controls[1].controls[1].content.controls[1].value = e.control.data.controls[2].value
            value.controls[0].content.controls[1].controls[0].content.controls[1].update()
            value.controls[0].content.controls[1].controls[1].content.controls[1].update()
            value.controls[0].content.controls[1].controls[2].content.controls[1].update()


def detailsfunctionscancel(e):
    for key, value in control_map.items():
        if key == 'AppFormFunctions':
            value.controls[0].content.controls[3].controls[0].content.visible = False
            value.controls[0].content.controls[3].controls[0].content.update()
            value.controls[0].content.controls[3].controls[1].content.visible = False
            value.controls[0].content.controls[3].controls[1].content.update()
            value.controls[0].content.controls[3].controls[2].content.disabled = False
            value.controls[0].content.controls[3].controls[2].content.update()
            value.controls[0].content.controls[0].controls[
                0].value = f"Gerenciamento de funções"
            value.controls[0].content.controls[0].controls[0].color = "black"
            value.controls[0].content.controls[0].controls[0].update()
            value.controls[0].content.controls[1].controls[0].content.controls[1].value = ""
            value.controls[0].content.controls[1].controls[1].content.controls[1].value = ""
            value.controls[0].content.controls[1].controls[2].content.controls[1].value = ""
            value.controls[0].content.controls[1].controls[0].content.controls[1].update()
            value.controls[0].content.controls[1].controls[1].content.controls[1].update()
            value.controls[0].content.controls[1].controls[2].content.controls[1].update()

def details(e):
    collaborator = e.control.data.controls[2].value
    for key, value in control_map.items():
        if key == 'AppForm':
            value.controls[0].content.controls[4].controls[0].content.visible = True
            value.controls[0].content.controls[4].controls[0].content.update()
            value.controls[0].content.controls[4].controls[1].content.visible = True
            value.controls[0].content.controls[4].controls[1].content.update()
            value.controls[0].content.controls[4].controls[2].content.disabled = True
            value.controls[0].content.controls[4].controls[2].content.update()
            value.controls[0].content.controls[2].controls[4].content.controls[1].value = e.control.data.controls[0].value
            value.controls[0].content.controls[2].controls[4].content.controls[1].update()
            value.controls[0].content.controls[1].controls[0].content.controls[1].value = e.control.data.controls[1].value
            value.controls[0].content.controls[1].controls[0].content.controls[1].update()
            value.controls[0].content.controls[1].controls[1].content.controls[1].value = e.control.data.controls[2].value
            value.controls[0].content.controls[1].controls[1].content.controls[1].update()
            value.controls[0].content.controls[1].controls[2].content.controls[1].value = e.control.data.controls[3].value
            value.controls[0].content.controls[1].controls[2].content.controls[1].update()
            value.controls[0].content.controls[2].controls[0].content.controls[1].value = e.control.data.controls[4].value
            value.controls[0].content.controls[2].controls[0].content.controls[1].update()
            value.controls[0].content.controls[2].controls[1].content.controls[1].value = e.control.data.controls[5].value
            value.controls[0].content.controls[2].controls[1].content.controls[1].update()
            value.controls[0].content.controls[2].controls[2].content.controls[1].value = e.control.data.controls[7].value
            value.controls[0].content.controls[2].controls[2].content.controls[1].update()
            value.controls[0].content.controls[2].controls[3].content.controls[1].value = e.control.data.controls[6].value
            value.controls[0].content.controls[2].controls[3].content.controls[1].update()
            value.controls[0].content.controls[0].controls[0].value = f"Editando informações do colaborador(a) {collaborator}"
            value.controls[0].content.controls[0].controls[0].color = "red"
            value.controls[0].content.controls[0].controls[0].update()

def detailscancel(e):
    for key, value in control_map.items():
        if key == 'AppForm':
            value.controls[0].content.controls[4].controls[0].content.visible = False
            value.controls[0].content.controls[4].controls[0].content.update()
            value.controls[0].content.controls[4].controls[1].content.visible = False
            value.controls[0].content.controls[4].controls[1].content.update()
            value.controls[0].content.controls[4].controls[2].content.disabled = False
            value.controls[0].content.controls[4].controls[2].content.update()
            value.controls[0].content.controls[1].controls[0].content.controls[1].value = ""
            value.controls[0].content.controls[1].controls[0].content.controls[1].update()
            value.controls[0].content.controls[1].controls[1].content.controls[1].value = ""
            value.controls[0].content.controls[1].controls[1].content.controls[1].update()
            value.controls[0].content.controls[1].controls[2].content.controls[1].value = ""
            value.controls[0].content.controls[1].controls[2].content.controls[1].update()
            value.controls[0].content.controls[2].controls[0].content.controls[1].value = ""
            value.controls[0].content.controls[2].controls[0].content.controls[1].update()
            value.controls[0].content.controls[2].controls[1].content.controls[1].value = ""
            value.controls[0].content.controls[2].controls[1].content.controls[1].update()
            value.controls[0].content.controls[2].controls[2].content.controls[1].value = ""
            value.controls[0].content.controls[2].controls[2].content.controls[1].update()
            value.controls[0].content.controls[2].controls[3].content.controls[1].value = ""
            value.controls[0].content.controls[2].controls[3].content.controls[1].update()
            value.controls[0].content.controls[2].controls[4].content.controls[1].value = ""
            value.controls[0].content.controls[2].controls[4].content.controls[1].update()
            value.controls[0].content.controls[0].controls[0].value = f"Gerenciamento de usuários"
            value.controls[0].content.controls[0].controls[0].color = "black"
            value.controls[0].content.controls[0].controls[0].update()

def addfunctions(e):
    for key, value in control_map.items():
        if key == 'AppFormFunctions':
            funcao = value.controls[0].content.controls[1].controls[0].content.controls[1].value
            nivel = value.controls[0].content.controls[1].controls[1].content.controls[1].value
            if not funcao:
                open_banner_error("Digite a função!", e)
            elif not nivel:
                open_banner_error("Selecione o nível da função!", e)
            else:
                SQLCodeInsert(f"INSERT INTO Funcoes ('funcao', 'nivel') VALUES ('{funcao.upper()}', '{nivel.upper()}')")
                value.controls[0].content.controls[1].controls[0].content.controls[1].value = ""
                value.controls[0].content.controls[1].controls[1].content.controls[1].value = ""
                value.controls[0].content.controls[1].controls[0].content.controls[1].update()
                value.controls[0].content.controls[1].controls[1].content.controls[1].update()
                open_banner_sucess("Função cadastrada com sucesso!", e)
                RunAndFilterQueryFunctions(e)

def updatefunctions(e):
    for key, value in control_map.items():
        if key == 'AppFormFunctions':
            funcao = value.controls[0].content.controls[1].controls[0].content.controls[1].value
            nivel = value.controls[0].content.controls[1].controls[1].content.controls[1].value
            id = value.controls[0].content.controls[1].controls[2].content.controls[1].value
            if not funcao:
                open_banner_error("Digite a função!", e)
            elif not nivel:
                open_banner_error("Selecione o nível da função!", e)
            else:
                SQLCodeUpdate(f"UPDATE Funcoes SET funcao = '{funcao.upper()}', nivel = '{nivel.upper()}' WHERE ID = '{id}' ", )
                detailsfunctionscancel(e)
                open_banner_sucess("Função editada com sucesso!", e)
                RunAndFilterQueryFunctions(e)

def add(e):
    for key, value in control_map.items():
        if key == 'AppForm':
            matricula = value.controls[0].content.controls[1].controls[0].content.controls[1].value
            nome = value.controls[0].content.controls[1].controls[1].content.controls[1].value
            funcao = value.controls[0].content.controls[1].controls[2].content.controls[1].value
            gestor = value.controls[0].content.controls[2].controls[0].content.controls[1].value
            turno = value.controls[0].content.controls[2].controls[1].content.controls[1].value
            area = value.controls[0].content.controls[2].controls[2].content.controls[1].value
            email = value.controls[0].content.controls[2].controls[3].content.controls[1].value
            if not matricula:
                open_banner_error("Digite o matrícula!", e)
            elif not matricula.isdigit() and matricula.upper() != "EXPERT":
                open_banner_error("A matrícula precisa ser um número ou o nome da agência!", e)
            elif len(matricula) < 5 and matricula.upper() != "EXPERT":
                open_banner_error("A matrícula precisa ter mais que 4 Digitos ou ser o nome da agência!", e)
            elif not input_name:
                open_banner_error("Digite o nome!", e)
            elif not " " in nome or len(nome) < 12:
                open_banner_error("Digite o nome completo!", e)
            elif not funcao:
                open_banner_error("Selecione a função!", e)
            elif not gestor:
                open_banner_error("Selecione o gestor!", e)
            elif not turno:
                open_banner_error("Selecione o turno!", e)
            elif not area:
                open_banner_error("Selecione a área!", e)
            elif email and not "@DHL.COM" in email.upper():
                open_banner_error("Precisa ser um e-mail DHL!", e)
            else:
                SQLCodeInsert(f"INSERT INTO Colaboradores ('matricula', 'nome', 'funcao', 'gestor', 'turno', 'setor', 'email') VALUES ('{matricula.upper()}', '{nome.upper()}', '{funcao.upper()}', '{gestor.upper()}', '{turno.upper()}', '{area.upper()}', '{email.upper()}')")
                value.controls[0].content.controls[1].controls[0].content.controls[1].value = ""
                value.controls[0].content.controls[1].controls[1].content.controls[1].value = ""
                value.controls[0].content.controls[1].controls[2].content.controls[1].value = ""
                value.controls[0].content.controls[2].controls[0].content.controls[1].value = ""
                value.controls[0].content.controls[2].controls[1].content.controls[1].value = ""
                value.controls[0].content.controls[2].controls[2].content.controls[1].value = ""
                value.controls[0].content.controls[2].controls[3].content.controls[1].value = ""
                value.controls[0].content.controls[2].controls[4].content.controls[1].value = ""
                value.controls[0].content.controls[1].controls[0].content.controls[1].update()
                value.controls[0].content.controls[1].controls[1].content.controls[1].update()
                value.controls[0].content.controls[1].controls[2].content.controls[1].update()
                value.controls[0].content.controls[2].controls[0].content.controls[1].update()
                value.controls[0].content.controls[2].controls[1].content.controls[1].update()
                value.controls[0].content.controls[2].controls[2].content.controls[1].update()
                value.controls[0].content.controls[2].controls[3].content.controls[1].update()
                value.controls[0].content.controls[2].controls[4].content.controls[1].update()
                open_banner_sucess("Colaborador cadastrado com sucesso!", e)
                RunAndFilterQuery(e)

def update(e):
    for key, value in control_map.items():
        if key == 'AppForm':
            matricula = value.controls[0].content.controls[1].controls[0].content.controls[1].value
            nome = value.controls[0].content.controls[1].controls[1].content.controls[1].value
            funcao = value.controls[0].content.controls[1].controls[2].content.controls[1].value
            gestor = value.controls[0].content.controls[2].controls[0].content.controls[1].value
            turno = value.controls[0].content.controls[2].controls[1].content.controls[1].value
            area = value.controls[0].content.controls[2].controls[2].content.controls[1].value
            email = value.controls[0].content.controls[2].controls[3].content.controls[1].value
            id = value.controls[0].content.controls[2].controls[4].content.controls[1].value
            if not matricula:
                open_banner_error("Digite o matrícula!", e)
            elif not matricula.isdigit() and matricula.upper() != "EXPERT":
                open_banner_error("A matrícula precisa ser um número ou o nome da agência!", e)
            elif len(matricula) < 5 and matricula.upper() != "EXPERT":
                open_banner_error("A matrícula precisa ter mais que 4 Digitos ou ser o nome da agência!", e)
            elif not input_name:
                open_banner_error("Digite o nome!", e)
            elif not " " in nome or len(nome) < 12:
                open_banner_error("Digite o nome completo!", e)
            elif not funcao:
                open_banner_error("Selecione a função!", e)
            elif not gestor:
                open_banner_error("Selecione o gestor!", e)
            elif not turno:
                open_banner_error("Selecione o turno!", e)
            elif not area:
                open_banner_error("Selecione a área!", e)
            elif email and not "@DHL.COM" in email.upper():
                open_banner_error("Precisa ser um e-mail DHL!", e)
            else:
                SQLCodeUpdate(f"UPDATE Colaboradores SET matricula = '{matricula.upper()}', nome = '{nome.upper()}', funcao = '{funcao.upper()}', gestor = '{gestor.upper()}', turno = '{turno.upper()}', setor = '{area.upper()}', email = '{email.upper()}' WHERE ID = '{id}' ", )
                open_banner_sucess("Alterações realizadas com sucesso!", e)
                detailscancel(e)
                RunAndFilterQuery(e)

class SearchInputCall(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("SearchInputCall", self)

    def build(self):
        self.app_form_input_instance()
        return Container(
            width=320,
            height=40,
            border=border.all(0.5, "#A9A9A9"),
            bgcolor="white10",
            border_radius=100,
            padding=8,
            opacity=1,
            animate_opacity=320,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=20, opacity=0.85, color="#A9A9A9"),
                    TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color=buttons_color,
                        focused_bgcolor="transparent",
                        focused_color=buttons_color,
                        filled="transparent",
                        keyboard_type=KeyboardType.NUMBER,
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color=buttons_color,
                        hint_text="Pesquisar",
                        hint_style=TextStyle(size=11, color="#A9A9A9"),
                        password=False,
                        on_change=lambda e: RunAndFilterQueryCall(e),  # lambda e: Pesquisar(e)
                    )

                ]
            )
        )

def InputedInSearchCall():
    for key, value in control_map.items():
        if key == "SearchInputCall":
            return value.controls[0].content.controls[1].value.lower()


class SearchInputSearch(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("SearchInputSearch", self)

    def build(self):
        self.app_form_input_instance()
        return Container(
            width=320,
            height=40,
            border=border.all(0.5, "#A9A9A9"),
            bgcolor="white10",
            border_radius=100,
            padding=8,
            opacity=1,
            animate_opacity=320,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=20, opacity=0.85, color="#A9A9A9"),
                    TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color=buttons_color,
                        focused_bgcolor="transparent",
                        focused_color=buttons_color,
                        filled="transparent",
                        keyboard_type=KeyboardType.NUMBER,
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color=buttons_color,
                        hint_text="Pesquisar",
                        hint_style=TextStyle(size=11, color="#A9A9A9"),
                        password=False,
                        on_change=lambda e: RunAndFilterSearch(e),  # lambda e: Pesquisar(e)
                    )

                ]
            )
        )

def InputedInSearchSearch():
    for key, value in control_map.items():
        if key == "SearchInputSearch":
            return value.controls[0].content.controls[1].value.lower()

class SearchInputFunctions(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("SearchInputFunctions", self)

    def build(self):
        self.app_form_input_instance()
        return Container(
            width=320,
            height=40,
            border=border.all(0.5, "#A9A9A9"),
            bgcolor="white10",
            border_radius=100,
            padding=8,
            opacity=1,
            animate_opacity=320,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=20, opacity=0.85, color="#A9A9A9"),
                    TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color=buttons_color,
                        focused_bgcolor="transparent",
                        focused_color=buttons_color,
                        filled="transparent",
                        keyboard_type=KeyboardType.NUMBER,
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color=buttons_color,
                        hint_text="Pesquisar",
                        hint_style=TextStyle(size=11, color="#A9A9A9"),
                        password=False,
                        on_change=lambda e: RunAndFilterQueryFunctions(e),  # lambda e: Pesquisar(e)
                    )

                ]
            )
        )

def InputedInSearchFunctions():
    for key, value in control_map.items():
        if key == "SearchInputFunctions":
            return value.controls[0].content.controls[1].value.lower()

class SearchInputCollaborators(UserControl):
    def __int__(self):
        super().__int__()

    def app_form_input_instance(self):
        add_to_control_reference("SearchInputCollaborators", self)

    def build(self):
        self.app_form_input_instance()
        return Container(
            width=320,
            height=40,
            border=border.all(0.5, "#A9A9A9"),
            bgcolor="white10",
            border_radius=100,
            padding=8,
            opacity=1,
            animate_opacity=320,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(name=icons.SEARCH_ROUNDED, size=20, opacity=0.85, color="#A9A9A9"),
                    TextField(
                        border_color='transparent',
                        bgcolor='transparent',
                        color=buttons_color,
                        focused_bgcolor="transparent",
                        focused_color=buttons_color,
                        filled="transparent",
                        keyboard_type=KeyboardType.NUMBER,
                        height=40,
                        width=290,
                        text_size=12,
                        content_padding=10,
                        cursor_color=buttons_color,
                        hint_text="Pesquisar",
                        hint_style=TextStyle(size=11, color="#A9A9A9"),
                        password=False,
                        on_change=lambda e: RunAndFilterQuery(e),  # lambda e: Pesquisar(e)
                    )

                ]
            )
        )

def InputedInSearchCollaborators():
    for key, value in control_map.items():
        if key == "SearchInputCollaborators":
            return value.controls[0].content.controls[1].value.lower()

def TableOneLines(value, result):
    for x in result:
        value.controls[0].controls[0].rows.append(
            DataRow(
                cells=[
                    DataCell(Text(x['matricula'])),
                    DataCell(Text(x['nome'])),
                    DataCell(IconButton(icon=icons.EDIT,
                                        icon_color=buttons_color,
                                        icon_size=20,
                                        on_click=details,
                                        tooltip="Mais detalhes",
                                        data=Row([
                                            Text(x['id']),
                                            Text(x['matricula']),
                                            Text(x['nome']),
                                            Text(x['funcao']),
                                            Text(x['gestor']),
                                            Text(x['turno']),
                                            Text(x['email']),
                                            Text(x['setor'])
                                        ]),
                                        )),
                    DataCell(IconButton(icon=icons.DELETE_FOREVER_ROUNDED,
                                        icon_color=buttons_color,
                                        icon_size=20,
                                        tooltip="Excluir colaborador",
                                        on_click=delete,
                                        data=Row([
                                            Text(x['id']),
                                            Text(x['matricula']),
                                            Text(x['nome']),
                                            Text(x['funcao']),
                                            Text(x['gestor']),
                                            Text(x['turno']),
                                            Text(x['email']),
                                            Text(x['setor'])

                                        ]),
                                        )),


                ],

            )
        )
        page.scroll = "always"
        value.controls[0].controls[0].update()

def TableOneLinesOMS(value, result):
    for x in result:
        value.controls[0].controls[0].rows.append(
            DataRow(
                cells=[
                    DataCell(Text(x['quantidade'])),
                    DataCell(Text(x['area'])),
                    DataCell(Text(x['turno'])),
                    DataCell(Text(x['presenteismo'])),
                    DataCell(IconButton(icon=icons.MORE_HORIZ_ROUNDED,
                                        icon_color=buttons_color,
                                        icon_size=20,
                                        on_click=DetailsOMS,
                                        tooltip="Mais detalhes",
                                        data=Row([
                                            Text(x['id']),
                                            Text(x['presenteismo']),
                                            Text(x['exame']),
                                            Text(x['suspensao']),
                                            Text(x['falecimento']),
                                            Text(x['ferias']),
                                            Text(x['atestado']),
                                            Text(x['falta']),
                                            Text(x['treinamento']),
                                            Text(x['desligado']),
                                            Text(x['sinergia']),
                                            Text(x['licenca']),
                                            Text(x['afastado']),
                                            Text(x['covid']),
                                            Text(x['transferido']),
                                            Text(x['folga']),
                                            Text(x['area']),
                                            Text(x['turno']),
                                            Text(x['gestor']),
                                            Text(x['quantidade']),
                                            Text(x['declaracao']),
                                        ]),
                                        )),
                    DataCell(IconButton(icon=icons.FILE_DOWNLOAD,
                                        icon_color=buttons_color,
                                        icon_size=20,
                                        tooltip="Excluir colaborador",
                                        on_click=processtoexcel,
                                        data=Row([
                                            Text(x['id']),
                                            Text(x['presenteismo']),
                                            Text(x['exame']),
                                            Text(x['suspensao']),
                                            Text(x['falecimento']),
                                            Text(x['ferias']),
                                            Text(x['atestado']),
                                            Text(x['falta']),
                                            Text(x['treinamento']),
                                            Text(x['desligado']),
                                            Text(x['sinergia']),
                                            Text(x['licenca']),
                                            Text(x['afastado']),
                                            Text(x['covid']),
                                            Text(x['transferido']),
                                            Text(x['folga']),
                                            Text(x['area']),
                                            Text(x['turno']),
                                            Text(x['gestor']),
                                            Text(x['quantidade']),
                                            Text(x['declaracao']),

                                        ]),
                                        )),


                ],

            )
        )
        page.scroll = "always"
        value.controls[0].controls[0].update()

def TableOneLinesFunctions(value, result):
    for x in result:
        value.controls[0].controls[0].rows.append(
            DataRow(
                cells=[
                    DataCell(Text(x['funcao'])),
                    DataCell(Text(x['nivel'])),
                    DataCell(IconButton(icon=icons.EDIT,
                                        icon_color=buttons_color,
                                        icon_size=20,
                                        on_click=detailsfunctions,
                                        tooltip="Mais detalhes",
                                        data=Row([
                                            Text(x['id']),
                                            Text(x['funcao']),
                                            Text(x['nivel']),

                                        ]),
                                        )),
                    DataCell(IconButton(icon=icons.DELETE_FOREVER_ROUNDED,
                                        icon_color=buttons_color,
                                        icon_size=20,
                                        tooltip="Excluir colaborador",
                                        on_click=deletefunctions,
                                        data=Row([
                                            Text(x['id']),
                                            Text(x['funcao']),
                                            Text(x['nivel']),
                                        ]),
                                        )),


                ],

            )
        )
        page.scroll = "always"
        value.controls[0].controls[0].update()

def TableOneLinesSearch(value, result):
    for x in result:
        value.controls[0].controls[0].rows.append(
            DataRow(
                cells=[
                    DataCell(Text(x['data'])),
                    DataCell(Text(x['nome'])),
                    DataCell(Text(x['status'])),
                    DataCell(Text(x['justificativa'])),
                    DataCell(Text(x['gestor'])),
                ],

            )
        )
        page.scroll = "always"
        value.controls[0].controls[0].update()

def SaveInformationsPresent(e):
    data = datecall.value
    matricula = e.control.data.controls[1].value
    nome = e.control.data.controls[2].value
    status = "PRESENTE"
    gestor = e.control.data.controls[4].value
    turno = e.control.data.controls[5].value
    area = e.control.data.controls[7].value
    if e.control.value == True:
        SQLCodeDeleteCall(data, nome)
        SQLCodeInsert(f"INSERT INTO Chamada ('data', 'matricula', 'nome', 'status', 'gestor', 'turno', 'setor') VALUES ('{data.upper()}', '{matricula.upper()}', '{nome.upper()}', '{status.upper()}', '{gestor.upper()}', '{turno.upper()}', '{area.upper()}')")
        SQLCodeInsertRastreabilidade(nome, status)
    if e.control.value == False:
        SQLCodeDeleteCall(data, nome)
        SQLCodeInsertRastreabilidade(nome, "EXCLUÍDO")
    RunAndFilterQueryCall(e)

justified = Dropdown(
        border_color="black",
        bgcolor=buttons_color,
        height=45,
        text_size=13,
        content_padding=10,
        color="black",
        options=[
            dropdown.Option("Suspensão"),
            dropdown.Option("Falecimento familiar"),
            dropdown.Option("Férias"),
            dropdown.Option("Exame periodíco"),
            dropdown.Option("Atestado"),
            dropdown.Option("Declaração"),
            dropdown.Option("Falta"),
            dropdown.Option("Treinamento"),
            dropdown.Option("Desligado"),
            dropdown.Option("Sinergia"),
            dropdown.Option("Licença"),
            dropdown.Option("Afastado"),
            dropdown.Option("Covid"),
            dropdown.Option("Transferido"),
            dropdown.Option("Folga"),
        ],
    )

def UpdateJustified(e):
    for key, value in control_map.items():
        if key == "AppFormCall":
            nome = value.controls[0].content.controls[1].controls[2].content.controls[0].value
    try:
        if justified.value == "":
            open_banner_error("Selecione uma justificativa!", e)
        else:
            SQLCodeUpdate(f"UPDATE Chamada  SET justificativa = '{justified.value.upper()}' WHERE data = '{datecall.value}' AND nome = '{nome}' ")
            connection = Connection()
            cursor = connection.cursor()
            cursor.execute(
                f"UPDATE RastrebilidadeChamada  SET justificativa = '{justified.value.upper()}' WHERE datadachamada = '{datecall.value}' AND colaborador = '{nome}' ", )
            connection.commit()
            connection.close()
            close_dlg(e)
            RunAndFilterQueryCall(e)
    except:
        open_banner_error("Não foi possível salvar a justificativa!", e)
        close_dlg(e)

def close_dlg(e):
    dlg_modal.open = False
    e.page.update()

dlg_modal = AlertDialog(
    modal=True,
    title=Text("Justificativa", size=15, color="black"),
    content=justified,
    actions=[
        TextButton("Salvar", on_click=UpdateJustified, style=ButtonStyle(color="white", bgcolor=buttons_color)),
    ],
    actions_alignment=MainAxisAlignment.END,
    on_dismiss=None,
 )

def open_dlg_modal(e):
    SaveInformationsJustified(e)
    for key, value in control_map.items():
        if key == "AppFormCall":
            value.controls[0].content.controls[1].controls[2].content.controls[0].value = e.control.data.controls[2].value
            value.controls[0].content.controls[1].controls[2].content.controls[0].update()
            e.page.update()
    if e.control.value == True:
        e.page.dialog = dlg_modal
        dlg_modal.open = True
        e.page.update()
        justified.value = ""
        justified.update()

def SaveInformationsJustified(e):
    data = datecall.value
    matricula = e.control.data.controls[1].value
    nome = e.control.data.controls[2].value
    status = "AUSENTE"
    gestor = e.control.data.controls[4].value
    turno = e.control.data.controls[5].value
    area = e.control.data.controls[7].value
    if e.control.value == True:
        SQLCodeDeleteCall(data, nome)
        SQLCodeInsert(f"INSERT INTO Chamada ('data', 'matricula', 'nome', 'status', 'gestor', 'turno', 'setor') VALUES ('{data.upper()}', '{matricula.upper()}', '{nome.upper()}', '{status.upper()}', '{gestor.upper()}', '{turno.upper()}', '{area.upper()}')")
        SQLCodeInsertRastreabilidade(nome, status)
    if e.control.value == False:
        SQLCodeDeleteCall(data, nome)
        SQLCodeInsertRastreabilidade(nome, "EXCLUÍDO")
    RunAndFilterQueryCall(e)

def TableOneLinesCall(value, result):
    for x in result:
        validation = SQLCodeSearch(f"""SELECT status FROM Chamada WHERE nome = '{x['nome']}' AND data = '{datecall.value}'""")
        chars = "[(',)]"
        validation = str(validation).translate(str.maketrans('', '', chars))
        if "PRESENTE" in validation:
            validationPresente = True
        else:
            validationPresente = False
        if "AUSENTE" in validation:
            validationAusente = True
        else:
            validationAusente = False
        value.controls[0].controls[0].rows.append(
            DataRow(
                cells=[
                    DataCell(Text(datecall.value)),
                    DataCell(Text(x['matricula'])),
                    DataCell(Text(x['nome'])),
                    DataCell(Checkbox(fill_color="white", check_color="green", data=Row([
                        Text(x['id']),
                        Text(x['matricula']),
                        Text(x['nome']),
                        Text(x['funcao']),
                        Text(x['gestor']),
                        Text(x['turno']),
                        Text(x['email']),
                        Text(x['setor'])
                    ]), on_change=SaveInformationsPresent, value=validationPresente)),
                    DataCell(Checkbox(fill_color="white", check_color="red", data=Row([
                        Text(x['id']),
                        Text(x['matricula']),
                        Text(x['nome']),
                        Text(x['funcao']),
                        Text(x['gestor']),
                        Text(x['turno']),
                        Text(x['email']),
                        Text(x['setor'])
                    ]), on_change=open_dlg_modal, value=validationAusente))

                ],

            )
        )
        page.scroll = "always"
        value.controls[0].controls[0].update()

def delete(e):
    SQLCodeDeleteCollaborators("Colaboradores", e.control.data.controls[0].value)
    open_banner_sucess("Colaborador excluído com sucesso!", e)
    RunAndFilterQuery(e)

def deletefunctions(e):
    SQLCodeDeleteCollaborators("Funcoes", e.control.data.controls[0].value)
    open_banner_sucess("Função excluída com sucesso!", e)
    RunAndFilterQueryFunctions(e)

def DataTableLines(key, users, value):
    if not users == "":
        keys = ['id', 'matricula', 'nome', 'funcao', 'gestor', 'turno', 'email', 'setor']
        result = [dict(zip(keys, values)) for values in users]
        value.controls[0].controls[0].rows.clear()
        TableOneLines(value, result)

def DataTableLinesOMS(key, users, value):
    if not users == "":
        keys = ['id', 'presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao']
        result = [dict(zip(keys, values)) for values in users]
        value.controls[0].controls[0].rows.clear()
        TableOneLinesOMS(value, result)

def DataTableLinesCall(key, users, value):
    if not users == "":
        keys = ['id', 'matricula', 'nome', 'funcao', 'gestor', 'turno', 'email', 'setor']
        result = [dict(zip(keys, values)) for values in users]
        value.controls[0].controls[0].rows.clear()
        TableOneLinesCall(value, result)

def DataTableLinesSearch(key, users, value):
    if not users == "":
        keys = ['id', 'data', 'matricula', 'nome', 'status', 'gestor', 'justificativa', 'turno', 'setor']
        result = [dict(zip(keys, values)) for values in users]
        value.controls[0].controls[0].rows.clear()
        TableOneLinesSearch(value, result)

def DataTableLinesFunctions(key, users, value):
    if not users == "":
        keys = ['id', 'funcao', 'nivel']
        result = [dict(zip(keys, values)) for values in users]
        value.controls[0].controls[0].rows.clear()
        TableOneLinesFunctions(value, result)

def RunAndFilterQuery(e):
    for key, value in control_map.items():
        Inputed = InputedInSearchCollaborators()
        if key == "AppDataTable":
            users = SQLCodeSearch(f"""SELECT * FROM Colaboradores WHERE nome != 'TODOS'""")
            if not Inputed:
                DataTableLines(key, users, value)
            else:
                search_name = InputedInSearchCollaborators()
                keys = ['id', 'matricula', 'nome', 'funcao', 'gestor', 'turno', 'email', 'setor']
                result = [dict(zip(keys, values)) for values in users]
                myfilter = list(filter(lambda x: search_name in x['nome'].lower(), result))
                if not Inputed == "":
                    if len(myfilter) > 0:
                        value.controls[0].controls[0].rows = []
                        TableOneLines(value, myfilter)
                    else:
                        value.controls[0].controls[0].update()
                else:
                    TableOneLines(value, result)

def RunAndFilterQueryOMST(e):
    for key, value in control_map.items():
        if key == "AppDataTableOMS":
            users = SQLCodeSearch(f"""SELECT * FROM Presenteismo""")
            DataTableLinesOMS(key, users, value)


def reset():
    for key, value in control_map.items():
        if key == "AppFormCall":
            value.controls[0].content.controls[1].controls[1].content.controls[1].value = ""
            value.controls[0].content.controls[1].controls[1].content.controls[1].update()


def RunAndFilterQueryCall(e):
    for key, value in control_map.items():
        if key == "AppFormCall":
            gestor = value.controls[0].content.controls[1].controls[1].content.controls[1].value
            if not datecall.value:
                reset()
                open_banner_error("Selecione a data da chamada!", e)
                reset()
            else:
                for key, value in control_map.items():
                    Inputed = InputedInSearchCall()
                    if key == "AppDataTableCall":
                        users = SQLCodeSearch(f"""SELECT * FROM Colaboradores WHERE gestor = '{gestor}'""")
                        if not Inputed:
                            DataTableLinesCall(key, users, value)
                        else:
                            search_name = InputedInSearchCall()
                            keys = ['id', 'matricula', 'nome', 'funcao', 'gestor', 'turno', 'email', 'setor']
                            result = [dict(zip(keys, values)) for values in users]
                            myfilter = list(filter(lambda x: search_name in x['nome'].lower(), result))
                            if not Inputed == "":
                                if len(myfilter) > 0:
                                    value.controls[0].controls[0].rows = []
                                    TableOneLinesCall(value, myfilter)
                                else:
                                    value.controls[0].controls[0].update()
                            else:
                                TableOneLinesCall(value, result)
def filterssearch():
    query = ""
    for key, value in control_map.items():
        if key == "AppFormSearch":
            status = value.controls[0].content.controls[1].controls[2].content.controls[1].value
            if status == "TODOS":
                query = SQLCodeSearch(f"""SELECT * FROM Chamada WHERE data BETWEEN '{datecall2.value}' AND '{datecall3.value}'""")
            else:
                query = SQLCodeSearch(
                    f"""SELECT * FROM Chamada WHERE data BETWEEN '{datecall2.value}' AND '{datecall3.value}' AND status = '{status}'""")
    return query


def RunAndFilterSearch(e):
    for key, value in control_map.items():
        Inputed = InputedInSearchSearch()
        if key == "AppDataTableSearch":
            users = filterssearch()
            if not Inputed:
                DataTableLinesSearch(key, users, value)
            else:
                search_name = InputedInSearchSearch()
                keys = ['id', 'data', 'matricula', 'nome', 'status', 'gestor', 'justificativa', 'turno', 'setor']
                result = [dict(zip(keys, values)) for values in users]
                myfilter = list(filter(lambda x: search_name in x['nome'].lower(), result))
                if not Inputed == "":
                    if len(myfilter) > 0:
                        value.controls[0].controls[0].rows = []
                        TableOneLinesSearch(value, myfilter)
                    else:
                        value.controls[0].controls[0].update()
                else:
                    TableOneLinesSearch(value, result)

def RunAndFilterQueryFunctions(e):
    for key, value in control_map.items():
        Inputed = InputedInSearchFunctions()
        if key == "AppDataTableFunctions":
            users = SQLCodeSearch(f"""SELECT * FROM Funcoes""")
            if not Inputed:
                DataTableLinesFunctions(key, users, value)
            else:
                search_name = InputedInSearchFunctions()
                keys = ['id', 'funcao', 'nivel']
                result = [dict(zip(keys, values)) for values in users]
                myfilter = list(filter(lambda x: search_name in x['funcao'].lower(), result))
                if not Inputed == "":
                    if len(myfilter) > 0:
                        value.controls[0].controls[0].rows = []
                        TableOneLinesFunctions(value, myfilter)
                    else:
                        value.controls[0].controls[0].update()
                else:
                    TableOneLinesFunctions(value, result)

def RunAndFilterQueryOMS(e):
    for key, value in control_map.items():
        if key == "AppFormOMS":
            gestor = value.controls[0].content.controls[2].controls[1].content.controls[1].value
            turno = value.controls[0].content.controls[1].controls[2].content.controls[1].value
            area = value.controls[0].content.controls[2].controls[0].content.controls[1].value
            datainicial = datecall4.value
            datafinal = datecall5.value
            if gestor == "TODOS" and area == "TODAS" and turno == "TODOS":
                AllTable(datainicial, datafinal)
                AllTablePresent(datainicial, datafinal)
                try:
                    PercentageWithoutFilters(datainicial, datafinal)
                except:
                    open_banner_error("Não há resultados para esse filtro!", e)
        
            elif gestor == "TODOS" and area == "TODAS" and turno != "TODOS":
                AllTableShift(datainicial, datafinal, turno.upper())
                AllTablePresentShift(datainicial, datafinal, turno.upper())
                try:
                    PercentageWithFilterShift(datainicial, datafinal, turno.upper())
                except:
                    open_banner_error("Não há resultados para esse filtro!", e)
        
            elif gestor == "TODOS" and area != "TODAS" and turno == "TODOS":
                AllTableArea(datainicial, datafinal, area.upper())
                AllTablePresentArea(datainicial, datafinal, area.upper())
                try:
                    PercentageWithFilterArea(datainicial, datafinal, area.upper())
                except:
                    open_banner_error("Não há resultados para esse filtro!", e)
        
            elif gestor != "TODOS" and area == "TODAS" and turno == "TODOS":
                AllTableCoordinator(datainicial, datafinal, gestor.upper())
                AllTablePresentCoordinator(datainicial, datafinal, gestor.upper())
                try:
                    PercentageWithFilterCoordinator(datainicial, datafinal, gestor.upper())
                except: open_banner_error("Não há resultados para esse filtro!", e)
        
            elif gestor == "TODOS" and area != "TODAS" and turno != "TODOS":
                AllTableShiftArea(datainicial, datafinal, turno.upper(), area.upper())
                AllTablePresentShiftArea(datainicial, datafinal, turno.upper(), area.upper())
                try:
                    PercentageWithFilterShiftArea(datainicial, datafinal, turno.upper(), area.upper())
                except:
                    open_banner_error("Não há resultados para esse filtro!", e)
        
            elif gestor != "TODOS" and area != "TODAS" and turno == "TODOS":
                AllTableAreaCoordinator(datainicial, datafinal, area.upper(), gestor.upper())
                AllTablePresentAreaCoordinator(datainicial, datafinal, area.upper(), gestor.upper())
                try:
                    PercentageWithFilterAreaCoordinator(datainicial, datafinal, area.upper(), gestor.upper())
                except:
                    open_banner_error("Não há resultados para esse filtro!", e)
        
            elif gestor != "TODOS" and area == "TODAS" and turno != "TODOS":
                AllTableShiftCoordinator(datainicial, datafinal, turno.upper(), gestor.upper())
                AllTablePresentShiftCoordinator(datainicial, datafinal, turno.upper(), gestor.upper())
                try:
                    PercentageWithFilterShiftCoordinator(datainicial, datafinal, turno.upper(), gestor.upper())
                except:
                    open_banner_error("Não há resultados para esse filtro!", e)
        
            elif gestor != "TODOS" and area != "TODAS" and turno != "TODOS":
                AllTableShiftAreaCoordinator(datainicial, datafinal, turno.upper(), area.upper(), gestor.upper())
                AllTablePresentShiftAreaCoordinator(datainicial, datafinal, turno.upper(), area.upper(), gestor.upper())
                try:
                    PercentageWithFilterShiftAreaCoordinator(datainicial, datafinal, turno.upper(), area.upper(), gestor.upper())
                except:
                    open_banner_error("Não há resultados para esse filtro!", e)
        
            else:
                pass
            RunAndFilterQueryOMST(e)

def DetailsOMS(e):
    for key, value in control_map.items():
        if key == "AppFormOMSInfos":
            value.controls[0].visible = True
            value.controls[0].update()
            value.controls[0].content.controls[0].controls[1].controls[0].content.controls[1].value = e.control.data.controls[2].value
            value.controls[0].content.controls[0].controls[1].controls[0].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[1].content.controls[1].value = e.control.data.controls[3].value
            value.controls[0].content.controls[0].controls[1].controls[1].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[2].content.controls[1].value = e.control.data.controls[4].value
            value.controls[0].content.controls[0].controls[1].controls[2].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[3].content.controls[1].value = e.control.data.controls[5].value
            value.controls[0].content.controls[0].controls[1].controls[3].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[4].content.controls[1].value = e.control.data.controls[6].value
            value.controls[0].content.controls[0].controls[1].controls[4].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[5].content.controls[1].value = e.control.data.controls[7].value
            value.controls[0].content.controls[0].controls[1].controls[5].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[6].content.controls[1].value = e.control.data.controls[8].value
            value.controls[0].content.controls[0].controls[1].controls[6].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[0].content.controls[1].value = e.control.data.controls[9].value
            value.controls[0].content.controls[0].controls[2].controls[0].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[1].content.controls[1].value = e.control.data.controls[10].value
            value.controls[0].content.controls[0].controls[2].controls[1].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[2].content.controls[1].value = e.control.data.controls[11].value
            value.controls[0].content.controls[0].controls[2].controls[2].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[3].content.controls[1].value = e.control.data.controls[12].value
            value.controls[0].content.controls[0].controls[2].controls[3].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[4].content.controls[1].value = e.control.data.controls[13].value
            value.controls[0].content.controls[0].controls[2].controls[4].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[5].content.controls[1].value = e.control.data.controls[14].value
            value.controls[0].content.controls[0].controls[2].controls[5].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[6].content.controls[1].value = e.control.data.controls[15].value
            value.controls[0].content.controls[0].controls[2].controls[6].content.controls[1].update()
            value.controls[0].content.controls[0].controls[3].controls[0].content.controls[1].value = e.control.data.controls[20].value
            value.controls[0].content.controls[0].controls[3].controls[0].content.controls[1].update()
    for key, value in control_map.items():
        if key == "AppFormOMS":
            value.controls[0].content.controls[4].controls[0].content.visible = True
            value.controls[0].content.controls[4].controls[0].content.update()
            value.controls[0].content.controls[4].controls[1].content.disabled = True
            value.controls[0].content.controls[4].controls[1].content.update()


def DetailsOMSCancel(e):
    for key, value in control_map.items():
        if key == "AppFormOMSInfos":
            value.controls[0].content.controls[0].controls[1].controls[0].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[1].controls[0].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[1].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[1].controls[1].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[2].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[1].controls[2].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[3].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[1].controls[3].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[4].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[1].controls[4].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[5].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[1].controls[5].content.controls[1].update()
            value.controls[0].content.controls[0].controls[1].controls[6].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[1].controls[6].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[0].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[2].controls[0].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[1].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[2].controls[1].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[2].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[2].controls[2].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[3].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[2].controls[3].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[4].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[2].controls[4].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[5].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[2].controls[5].content.controls[1].update()
            value.controls[0].content.controls[0].controls[2].controls[6].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[2].controls[6].content.controls[1].update()
            value.controls[0].content.controls[0].controls[3].controls[0].content.controls[1].value = ""
            value.controls[0].content.controls[0].controls[3].controls[0].content.controls[1].update()
            value.controls[0].visible = False
            value.controls[0].update()
    for key, value in control_map.items():
        if key == "AppFormOMS":
            value.controls[0].content.controls[4].controls[0].content.visible = False
            value.controls[0].content.controls[4].controls[0].content.update()
            value.controls[0].content.controls[4].controls[1].content.disabled = False
            value.controls[0].content.controls[4].controls[1].content.update()

def processtoexcel(e):
    users = SQLCodeSearch(f"""SELECT * FROM Presenteismo""")
    keys = ['id', 'presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao']
    if not users == []:
        result = [dict(zip(keys, values)) for values in users]
        data = {'ID': [], 'AREA': [], 'TURNO': [], 'GESTOR': [], 'QUANTIDADE': [], 'PRESENTEISMO': [], 'EXAME MEDICO': [], 'SUSPENSAO': [], 'FALECIMENTOF': [], 'FERIAS': [], 'ATESTADO': [], 'FALTA': [], 'TREINAMENTO': [], 'DESLIGADO': [], 'SINERGIA': [], 'LICENCA': [], 'AFASTADO': [], 'COVID': [], 'TRANSFERIDO': [], 'FOLGA': [], 'DECLARAÇÃO': [],}
        for x in result:
            data['QUANTIDADE'].append(x['quantidade']),
            data['AREA'].append(x['area']),
            data['TURNO'].append(x['turno']),
            data['GESTOR'].append(x['gestor']),
            data['ID'].append(x['id']),
            data['PRESENTEISMO'].append(x['presenteismo']),
            data['EXAME MEDICO'].append(x['exame']),
            data['SUSPENSAO'].append(x['suspensao']),
            data['FALECIMENTOF'].append(x['falecimento']),
            data['FERIAS'].append(x['ferias']),
            data['ATESTADO'].append(x['atestado']),
            data['FALTA'].append(x['falta']),
            data['TREINAMENTO'].append(x['treinamento']),
            data['DESLIGADO'].append(x['desligado']),
            data['SINERGIA'].append(x['sinergia']),
            data['LICENCA'].append(x['licenca']),
            data['AFASTADO'].append(x['afastado']),
            data['COVID'].append(x['covid']),
            data['TRANSFERIDO'].append(x['transferido']),
            data['FOLGA'].append(x['folga']),
            data['DECLARAÇÃO'].append(x['declaracao']),
        df = pd.DataFrame(data)
        df.to_excel("RelatorioOMS.xlsx", index=False)
        open_banner_downloadOMS("Download realizado com sucesso", e)
    else:
        pass

def processtoexcelcall(e):
    users = SQLCodeSearch(f"""SELECT * FROM Chamada""")
    keys = ['id', 'data', 'matricula', 'nome', 'status', 'gestor', 'justificativa', 'turno', 'setor']
    if not users == []:
        result = [dict(zip(keys, values)) for values in users]
        data = {'ID': [], 'DATA': [], 'MATRICULA': [], 'NOME': [], 'STATUS': [], 'GESTOR': [], 'JUSTIFICATIVA': [], 'TURNO': [], 'SETOR': [],}
        for x in result:
            data['ID'].append(x['id']),
            data['DATA'].append(x['data']),
            data['MATRICULA'].append(x['matricula']),
            data['NOME'].append(x['nome']),
            data['STATUS'].append(x['status']),
            data['GESTOR'].append(x['gestor']),
            data['JUSTIFICATIVA'].append(x['justificativa']),
            data['TURNO'].append(x['turno']),
            data['SETOR'].append(x['setor']),
        df = pd.DataFrame(data)
        df.to_excel("RelatorioChamada.xlsx", index=False)
        open_banner_downloadCall("Download realizado com sucesso", e)
    else:
        pass

def processtoexcelcollaborators(e):
    users = SQLCodeSearch(f"""SELECT * FROM Colaboradores""")
    keys = ['id', 'matricula', 'nome', 'funcao', 'gestor', 'turno', 'email', 'setor']
    if not users == []:
        result = [dict(zip(keys, values)) for values in users]
        data = {'ID': [], 'MATRICULA': [], 'NOME': [], 'FUNCAO': [], 'GESTOR': [], 'TURNO': [], 'EMAIL': [], 'SETOR': [],}
        for x in result:
            data['ID'].append(x['id']),
            data['MATRICULA'].append(x['matricula']),
            data['NOME'].append(x['nome']),
            data['FUNCAO'].append(x['funcao']),
            data['GESTOR'].append(x['gestor']),
            data['TURNO'].append(x['turno']),
            data['EMAIL'].append(x['email']),
            data['SETOR'].append(x['setor']),
        df = pd.DataFrame(data)
        df.to_excel("RelatorioColaboradores.xlsx", index=False)
        open_banner_downloadCollaborators("Download realizado com sucesso", e)
    else:
        pass