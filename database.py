import sqlite3
from configurations import *
import getpass
from dateinput import View_date as datecall
import datetime

def Connection():
    return sqlite3.connect(f'C:/Users/{getpass.getuser()}/DPDHL/Reckitt Itupeva - Controle de presença/Configurações/Banco de dados/ListaPresenca.db')


def SQLCodeSearch(sql):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(f"""{sql}""", )
    data = cursor.fetchall()
    connection.close()
    return data

#Duas grades separadas, uma para
input_name = "Airton"

def SQLCodeInsert(sql):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def SQLCodeUpdate(sql):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def SQLCodeDeleteCollaborators(tabela, id):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {tabela} WHERE id=?",
                (id,))
    connection.commit()
    connection.close()

def SQLCodeDeleteCall(date, nome):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM Chamada WHERE data=? AND nome=?",
        (date, nome,))
    connection.commit()
    connection.close()

def SQLCodeInsertRastreabilidade(nome, status):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO RastrebilidadeChamada ('aplicadopor', 'datadaaplicacao', 'datadachamada', 'colaborador', 'status') VALUES (?,?,?,?,?)",
        (f'{getpass.getuser()}', f'{datetime.datetime.now()}', f'{datecall.value}', f'{nome}', f'{status}',))
    connection.commit()
    connection.close()

