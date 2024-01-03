from flet import *
from form import AppForm, AppFormCall, AppFormSearch, AppFormFunctions, AppFormOMS, AppFormOMSInfos
from data_table import AppDataTable, AppDataTableCall, AppDataTableSearch, AppDataTableFunctions, AppDataTableOMS
from header import *
from TablesLines import SearchInputCall, SearchInputCollaborators, SearchInputSearch, SearchInputFunctions, processtoexcelcall, processtoexcelcollaborators

ScreenCollaborators = Column(
                    expand=True,
                    visible=False,
                    alignment=alignment.top_center,
                    controls=[
                        #AppHeader(),
                        AppForm(),
                        Row([
                        SearchInputCollaborators(),
                        Container(content=IconButton(icons.DOWNLOAD, icon_color=buttons_color, icon_size=20, on_click=processtoexcelcollaborators))
                            ]),
                    Column([
                        AppDataTable(),
                    ], scroll="hidden",
                    expand=True,)

                    ]
                )

ScreenCall = Column(
                    expand=True,
                    visible=False,
                    alignment=alignment.top_center,
                    controls=[
                        #AppHeader(),
                        AppFormCall(),
                        SearchInputCall(),
                    Column([
                        AppDataTableCall(),
                    ], scroll="hidden",
                    expand=True,)

                    ]
                )

ScreenSearch = Column(
                    expand=True,
                    visible=True,
                    alignment=alignment.top_center,
                    controls=[
                        #AppHeader(),
                        AppFormSearch(),
                        Row([
                        SearchInputSearch(),
                        Container(content=IconButton(icons.DOWNLOAD, icon_color=buttons_color, icon_size=20, on_click=processtoexcelcall))
                            ]),
                    Column([
                        AppDataTableSearch(),
                    ], scroll="hidden",
                    expand=True,)

                    ]
                )

ScreenFunctions = Column(
                    expand=True,
                    visible=False,
                    alignment=alignment.top_center,
                    controls=[
                        #AppHeader(),
                        AppFormFunctions(),
                        SearchInputFunctions(),
                    Column([
                        AppDataTableFunctions(),
                    ], scroll="hidden",
                    expand=True,)

                    ]
                )

ScreenOMS = Column(
                    expand=True,
                    visible=False,
                    alignment=alignment.top_center,
                    controls=[
                        #AppHeader(),
                        AppFormOMS(),
                    Column([
                        AppDataTableOMS(),
                        AppFormOMSInfos(),
                    ], scroll="hidden",
                    expand=True,),

                    ]
                )