from flet import *
from controls import add_to_control_reference
from configurations import *

class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()


    def app_data_table_instance(self):
        add_to_control_reference("AppDataTable", self)

    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text("Matrícula", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Nome", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Editar", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Excluir", size=12, color="black", weight="bold")
                        ),

                    ],
                    rows=[]
                )
            ]
        )


class AppDataTableCall(UserControl):
    def __init__(self):
        super().__init__()


    def app_data_table_instance(self):
        add_to_control_reference("AppDataTableCall", self)

    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text("Data", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Matrícula", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Nome", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Presente", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Ausente", size=12, color="black", weight="bold")
                        ),

                    ],
                    rows=[]
                )
            ]
        )

class AppDataTableSearch(UserControl):
    def __init__(self):
        super().__init__()


    def app_data_table_instance(self):
        add_to_control_reference("AppDataTableSearch", self)

    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text("Data", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Nome", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Status", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Justificativa", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Gestor", size=12, color="black", weight="bold")
                        ),

                    ],
                    rows=[]
                )
            ]
        )

class AppDataTableFunctions(UserControl):
    def __init__(self):
        super().__init__()


    def app_data_table_instance(self):
        add_to_control_reference("AppDataTableFunctions", self)

    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text("Função", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Nível", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Editar", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Excluir", size=12, color="black", weight="bold")
                        ),
                    ],
                    rows=[]
                )
            ]
        )

class AppDataTableOMS(UserControl):
    def __init__(self):
        super().__init__()


    def app_data_table_instance(self):
        add_to_control_reference("AppDataTableOMS", self)

    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text("Colaboradores", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Área", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Turno", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Presenteísmo", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Detalhes", size=12, color="black", weight="bold")
                        ),
                        DataColumn(
                            Text("Download", size=12, color="black", weight="bold")
                        ),
                    ],
                    rows=[]
                )
            ]
        )