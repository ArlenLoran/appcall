import sqlite3
from database import *


def AllTable(InitialDate, FinalDate):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTableShift(InitialDate, FinalDate, Shift):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND turno = '{Shift}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTableShiftArea(InitialDate, FinalDate, Shift, Area):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND turno = '{Shift}' AND setor = '{Area}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTableShiftAreaCoordinator(InitialDate, FinalDate, Shift, Area, coordinator):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND turno = '{Shift}' AND setor = '{Area}' AND gestor = '{coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTableArea(InitialDate, FinalDate, Area):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND setor = '{Area}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTableAreaCoordinator(InitialDate, FinalDate, Area, coordinator):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND setor = '{Area}' AND gestor = '{coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTableShiftCoordinator(InitialDate, FinalDate, Shift, coordinator):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND turno = '{Shift}' AND gestor = '{coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTableCoordinator(InitialDate, FinalDate, coordinator):
    connenction = Connection()
    cursor = connenction.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND gestor = '{coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connenction.close()
    return validation


def AllTablePresent(InitialDate, FinalDate):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def AllTablePresentShift(InitialDate, FinalDate, Shift):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' AND turno = '{Shift}' """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def AllTablePresentShiftArea(InitialDate, FinalDate, Shift, Area):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' AND turno = '{Shift}' AND setor = '{Area}' """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def AllTablePresentShiftAreaCoordinator(InitialDate, FinalDate, Shift, Area, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' AND turno = '{Shift}' AND setor = '{Area}' AND gestor = '{Coordinator}'  """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def AllTablePresentArea(InitialDate, FinalDate, Area):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' AND setor = '{Area}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def AllTablePresentAreaCoordinator(InitialDate, FinalDate, Area, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' AND setor = '{Area}' AND gestor = '{Coordinator}'  """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def AllTablePresentShiftCoordinator(InitialDate, FinalDate, Shift, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' AND turno = '{Shift}' AND gestor = '{Coordinator}'  """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def AllTablePresentCoordinator(InitialDate, FinalDate, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    # fetch all the data and store it in a variable
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND status = 'PRESENTE' AND gestor = '{Coordinator}'  """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    connection.close()
    return validation


def TableWithFilter(filter, InitialDate, FinalDate):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(AllTable(InitialDate, FinalDate))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def TableWithFilterShift(filter, InitialDate, FinalDate, Shift):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' AND turno = '{Shift}' """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(AllTableShift(InitialDate, FinalDate, Shift))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def TableWithFilterShiftArea(filter, InitialDate, FinalDate, Shift, Area):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' AND turno = '{Shift}' AND setor = '{Area}' """, )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(AllTableShiftArea(InitialDate, FinalDate, Shift, Area))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def TableWithFilterShiftAreaCoordinator(filter, InitialDate, FinalDate, Shift, Area, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' AND turno = '{Shift}' AND setor = '{Area}' AND gestor = '{Coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(
            AllTableShiftAreaCoordinator(InitialDate, FinalDate, Shift, Area, Coordinator))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def TableWithFilterAreaCoordinator(filter, InitialDate, FinalDate, Area, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' AND setor = '{Area}' AND gestor = '{Coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(AllTableAreaCoordinator(InitialDate, FinalDate, Area, Coordinator))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def TableWithFilterArea(filter, InitialDate, FinalDate, Area):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' AND setor = '{Area}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(AllTableArea(InitialDate, FinalDate, Area))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def TableWithFilterShiftCoordinator(filter, InitialDate, FinalDate, Shift, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' AND turno = '{Shift}' AND gestor = '{Coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(AllTableShiftCoordinator(InitialDate, FinalDate, Shift, Coordinator))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def TableWithFilterCoordinator(filter, InitialDate, FinalDate, Coordinator):
    connection = Connection()
    cursor = connection.cursor()
    result = cursor.execute(
        f"""SELECT Count(*) FROM chamada WHERE data BETWEEN '{InitialDate}' AND '{FinalDate}' AND  justificativa = '{filter}' AND gestor = '{Coordinator}'""", )
    users = result.fetchall()
    chars = "[(',)]"
    validation = str(users).translate(str.maketrans('', '', chars))
    try:
        validation = int(validation) / int(AllTableCoordinator(InitialDate, FinalDate, Coordinator))
    except:
        pass
    validation = validation * 100
    connection.close()
    return validation


def PercentageWithoutFilters(ttdatainicial, ttdatafinal):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTable(ttdatainicial, ttdatafinal)
    TotalPresent = AllTablePresent(ttdatainicial, ttdatafinal)
    TotalExam = TableWithFilter("EXAME PERIODÍCO", ttdatainicial, ttdatafinal)
    TotalSuspended = TableWithFilter("SUSPENSÃO", ttdatainicial, ttdatafinal)
    TotalDeath = TableWithFilter("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal)
    TotalVacation = TableWithFilter("FÉRIAS", ttdatainicial, ttdatafinal)
    TotalCertificate = TableWithFilter("ATESTADO", ttdatainicial, ttdatafinal)
    TotalDeclaration = TableWithFilter("DECLARAÇÃO", ttdatainicial, ttdatafinal)
    TotalAbsence = TableWithFilter("FALTA", ttdatainicial, ttdatafinal)
    TotalTraining = TableWithFilter("TREINAMENTO", ttdatainicial, ttdatafinal)
    TotalOff = TableWithFilter("DESLIGADO", ttdatainicial, ttdatafinal)
    TotalSynergy = TableWithFilter("SINERGIA", ttdatainicial, ttdatafinal)
    TotalLicense = TableWithFilter("LICENÇA", ttdatainicial, ttdatafinal)
    TotalAway = TableWithFilter("AFASTADO", ttdatainicial, ttdatafinal)
    TotalCovid = TableWithFilter("COVID", ttdatainicial, ttdatafinal)
    TotalTransferred = TableWithFilter("TRANSFERIDO", ttdatainicial, ttdatafinal)
    TotalDayOff = TableWithFilter("FOLGA", ttdatainicial, ttdatafinal)
    try:
        AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    except:
        AttendancePercentage = str(0)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', 'Todas', 'Todos', 'Todos', f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()


def PercentageWithFilterShift(ttdatainicial, ttdatafinal, ttturno):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTableShift(ttdatainicial, ttdatafinal, ttturno)
    TotalPresent = AllTablePresentShift(ttdatainicial, ttdatafinal, ttturno)
    TotalExam = TableWithFilterShift("EXAME PERIODÍCO", ttdatainicial, ttdatafinal, ttturno)
    TotalSuspended = TableWithFilterShift("SUSPENSÃO", ttdatainicial, ttdatafinal, ttturno)
    TotalDeath = TableWithFilterShift("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal, ttturno)
    TotalVacation = TableWithFilterShift("FÉRIAS", ttdatainicial, ttdatafinal, ttturno)
    TotalCertificate = TableWithFilterShift("ATESTADO", ttdatainicial, ttdatafinal, ttturno)
    TotalDeclaration = TableWithFilterShift("DECLARAÇÃO", ttdatainicial, ttdatafinal, ttturno)
    TotalAbsence = TableWithFilterShift("FALTA", ttdatainicial, ttdatafinal, ttturno)
    TotalTraining = TableWithFilterShift("TREINAMENTO", ttdatainicial, ttdatafinal, ttturno)
    TotalOff = TableWithFilterShift("DESLIGADO", ttdatainicial, ttdatafinal, ttturno)
    TotalSynergy = TableWithFilterShift("SINERGIA", ttdatainicial, ttdatafinal, ttturno)
    TotalLicense = TableWithFilterShift("LICENÇA", ttdatainicial, ttdatafinal, ttturno)
    TotalAway = TableWithFilterShift("AFASTADO", ttdatainicial, ttdatafinal, ttturno)
    TotalCovid = TableWithFilterShift("COVID", ttdatainicial, ttdatafinal, ttturno)
    TotalTransferred = TableWithFilterShift("TRANSFERIDO", ttdatainicial, ttdatafinal, ttturno)
    TotalDayOff = TableWithFilterShift("FOLGA", ttdatainicial, ttdatafinal, ttturno)
    AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', 'Todas', f'{ttturno.capitalize()}', 'Todos', f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()


def PercentageWithFilterShiftArea(ttdatainicial, ttdatafinal, ttturno, ttarea):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTableShiftArea(ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalPresent = AllTablePresentShiftArea(ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalExam = TableWithFilterShiftArea("EXAME PERIODÍCO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalSuspended = TableWithFilterShiftArea("SUSPENSÃO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalDeath = TableWithFilterShiftArea("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalVacation = TableWithFilterShiftArea("FÉRIAS", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalCertificate = TableWithFilterShiftArea("ATESTADO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalDeclaration = TableWithFilterShiftArea("DECLARAÇÃO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalAbsence = TableWithFilterShiftArea("FALTA", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalTraining = TableWithFilterShiftArea("TREINAMENTO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalOff = TableWithFilterShiftArea("DESLIGADO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalSynergy = TableWithFilterShiftArea("SINERGIA", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalLicense = TableWithFilterShiftArea("LICENÇA", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalAway = TableWithFilterShiftArea("AFASTADO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalCovid = TableWithFilterShiftArea("COVID", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalTransferred = TableWithFilterShiftArea("TRANSFERIDO", ttdatainicial, ttdatafinal, ttturno, ttarea)
    TotalDayOff = TableWithFilterShiftArea("FOLGA", ttdatainicial, ttdatafinal, ttturno, ttarea)
    AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', f'{ttarea.capitalize()}', f'{ttturno.capitalize()}', 'Todos', f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()


def PercentageWithFilterShiftAreaCoordinator(ttdatainicial, ttdatafinal, ttturno, ttarea, ttcoordinator):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTableShiftAreaCoordinator(ttdatainicial, ttdatafinal, ttturno, ttarea, ttcoordinator)
    TotalPresent = AllTablePresentShiftAreaCoordinator(ttdatainicial, ttdatafinal, ttturno, ttarea, ttcoordinator)
    TotalExam = TableWithFilterShiftAreaCoordinator("EXAME PERIODÍCO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                    ttcoordinator)
    TotalSuspended = TableWithFilterShiftAreaCoordinator("SUSPENSÃO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                         ttcoordinator)
    TotalDeath = TableWithFilterShiftAreaCoordinator("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal, ttturno,
                                                     ttarea, ttcoordinator)
    TotalVacation = TableWithFilterShiftAreaCoordinator("FÉRIAS", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                        ttcoordinator)
    TotalCertificate = TableWithFilterShiftAreaCoordinator("ATESTADO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                           ttcoordinator)
    TotalDeclaration = TableWithFilterShiftAreaCoordinator("DECLARAÇÃO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                           ttcoordinator)
    TotalAbsence = TableWithFilterShiftAreaCoordinator("FALTA", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                       ttcoordinator)
    TotalTraining = TableWithFilterShiftAreaCoordinator("TREINAMENTO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                        ttcoordinator)
    TotalOff = TableWithFilterShiftAreaCoordinator("DESLIGADO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                   ttcoordinator)
    TotalSynergy = TableWithFilterShiftAreaCoordinator("SINERGIA", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                       ttcoordinator)
    TotalLicense = TableWithFilterShiftAreaCoordinator("LICENÇA", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                       ttcoordinator)
    TotalAway = TableWithFilterShiftAreaCoordinator("AFASTADO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                    ttcoordinator)
    TotalCovid = TableWithFilterShiftAreaCoordinator("COVID", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                     ttcoordinator)
    TotalTransferred = TableWithFilterShiftAreaCoordinator("TRANSFERIDO", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                           ttcoordinator)
    TotalDayOff = TableWithFilterShiftAreaCoordinator("FOLGA", ttdatainicial, ttdatafinal, ttturno, ttarea,
                                                      ttcoordinator)
    AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', f'{ttarea.capitalize()}', f'{ttturno.capitalize()}', f'{ttcoordinator.upper()}',
        f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()


def PercentageWithFilterCoordinator(ttdatainicial, ttdatafinal, ttcoordinator):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTableCoordinator(ttdatainicial, ttdatafinal, ttcoordinator)
    TotalPresent = AllTablePresentCoordinator(ttdatainicial, ttdatafinal, ttcoordinator)
    TotalExam = TableWithFilterCoordinator("EXAME PERIODÍCO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalSuspended = TableWithFilterCoordinator("SUSPENSÃO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalDeath = TableWithFilterCoordinator("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalVacation = TableWithFilterCoordinator("FÉRIAS", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalCertificate = TableWithFilterCoordinator("ATESTADO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalDeclaration = TableWithFilterCoordinator("DECLARAÇÃO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalAbsence = TableWithFilterCoordinator("FALTA", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalTraining = TableWithFilterCoordinator("TREINAMENTO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalOff = TableWithFilterCoordinator("DESLIGADO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalSynergy = TableWithFilterCoordinator("SINERGIA", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalLicense = TableWithFilterCoordinator("LICENÇA", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalAway = TableWithFilterCoordinator("AFASTADO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalCovid = TableWithFilterCoordinator("COVID", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalTransferred = TableWithFilterCoordinator("TRANSFERIDO", ttdatainicial, ttdatafinal, ttcoordinator)
    TotalDayOff = TableWithFilterCoordinator("FOLGA", ttdatainicial, ttdatafinal, ttcoordinator)
    AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', 'Todas', 'Todos', f'{ttcoordinator.upper()}', f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()


def PercentageWithFilterShiftCoordinator(ttdatainicial, ttdatafinal, ttturno, ttcoordinator):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTableShiftCoordinator(ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalPresent = AllTablePresentShiftCoordinator(ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalExam = TableWithFilterShiftCoordinator("EXAME PERIODÍCO", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalSuspended = TableWithFilterShiftCoordinator("SUSPENSÃO", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalDeath = TableWithFilterShiftCoordinator("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalVacation = TableWithFilterShiftCoordinator("FÉRIAS", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalCertificate = TableWithFilterShiftCoordinator("ATESTADO", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalDeclaration = TableWithFilterShiftCoordinator("DECLARAÇÃO", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalAbsence = TableWithFilterShiftCoordinator("FALTA", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalTraining = TableWithFilterShiftCoordinator("TREINAMENTO", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalOff = TableWithFilterShiftCoordinator("DESLIGADO", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalSynergy = TableWithFilterShiftCoordinator("SINERGIA", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalLicense = TableWithFilterShiftCoordinator("LICENÇA", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalAway = TableWithFilterShiftCoordinator("AFASTADO", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalCovid = TableWithFilterShiftCoordinator("COVID", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    TotalTransferred = TableWithFilterShiftCoordinator("TRANSFERIDO", ttdatainicial, ttdatafinal, ttturno,
                                                       ttcoordinator)
    TotalDayOff = TableWithFilterShiftCoordinator("FOLGA", ttdatainicial, ttdatafinal, ttturno, ttcoordinator)
    AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', 'Todas', f'{ttturno.capitalize()}', f'{ttcoordinator.upper()}', f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()


def PercentageWithFilterAreaCoordinator(ttdatainicial, ttdatafinal, ttarea, ttcoordinator):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTableAreaCoordinator(ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalPresent = AllTablePresentAreaCoordinator(ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalExam = TableWithFilterAreaCoordinator("EXAME PERIODÍCO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalSuspended = TableWithFilterAreaCoordinator("SUSPENSÃO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalDeath = TableWithFilterAreaCoordinator("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalVacation = TableWithFilterAreaCoordinator("FÉRIAS", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalCertificate = TableWithFilterAreaCoordinator("ATESTADO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalDeclaration = TableWithFilterAreaCoordinator("DECLARAÇÃO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalAbsence = TableWithFilterAreaCoordinator("FALTA", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalTraining = TableWithFilterAreaCoordinator("TREINAMENTO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalOff = TableWithFilterAreaCoordinator("DESLIGADO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalSynergy = TableWithFilterAreaCoordinator("SINERGIA", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalLicense = TableWithFilterAreaCoordinator("LICENÇA", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalAway = TableWithFilterAreaCoordinator("AFASTADO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalCovid = TableWithFilterAreaCoordinator("COVID", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalTransferred = TableWithFilterAreaCoordinator("TRANSFERIDO", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    TotalDayOff = TableWithFilterAreaCoordinator("FOLGA", ttdatainicial, ttdatafinal, ttarea, ttcoordinator)
    AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', f'{ttarea.capitalize()}', 'Todos', f'{ttcoordinator.upper()}', f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()


def PercentageWithFilterArea(ttdatainicial, ttdatafinal, ttarea):
    connection = Connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Presenteismo WHERE id > 0")
    connection.commit()
    connection.close()
    GrandTotal = AllTableArea(ttdatainicial, ttdatafinal, ttarea)
    TotalPresent = AllTablePresentArea(ttdatainicial, ttdatafinal, ttarea)
    TotalExam = TableWithFilterArea("EXAME PERIODÍCO", ttdatainicial, ttdatafinal, ttarea)
    TotalSuspended = TableWithFilterArea("SUSPENSÃO", ttdatainicial, ttdatafinal, ttarea)
    TotalDeath = TableWithFilterArea("FALECIMENTO FAMILIAR", ttdatainicial, ttdatafinal, ttarea)
    TotalVacation = TableWithFilterArea("FÉRIAS", ttdatainicial, ttdatafinal, ttarea)
    TotalCertificate = TableWithFilterArea("ATESTADO", ttdatainicial, ttdatafinal, ttarea)
    TotalDeclaration = TableWithFilterArea("DECLARAÇÃO", ttdatainicial, ttdatafinal, ttarea)
    TotalAbsence = TableWithFilterArea("FALTA", ttdatainicial, ttdatafinal, ttarea)
    TotalTraining = TableWithFilterArea("TREINAMENTO", ttdatainicial, ttdatafinal, ttarea)
    TotalOff = TableWithFilterArea("DESLIGADO", ttdatainicial, ttdatafinal, ttarea)
    TotalSynergy = TableWithFilterArea("SINERGIA", ttdatainicial, ttdatafinal, ttarea)
    TotalLicense = TableWithFilterArea("LICENÇA", ttdatainicial, ttdatafinal, ttarea)
    TotalAway = TableWithFilterArea("AFASTADO", ttdatainicial, ttdatafinal, ttarea)
    TotalCovid = TableWithFilterArea("COVID", ttdatainicial, ttdatafinal, ttarea)
    TotalTransferred = TableWithFilterArea("TRANSFERIDO", ttdatainicial, ttdatafinal, ttarea)
    TotalDayOff = TableWithFilterArea("FOLGA", ttdatainicial, ttdatafinal, ttarea)
    AttendancePercentage = int(TotalPresent) / int(GrandTotal)
    FiltersDisregarded = TotalVacation + TotalDayOff + TotalExam + TotalTraining + TotalOff + TotalSynergy + TotalLicense + TotalAway + TotalTransferred
    FinalPercentage = str((AttendancePercentage * 100) + FiltersDisregarded)
    JustSixDigits = FinalPercentage[:6]
    Presenteeism = f'{JustSixDigits}%'
    exam = str(TotalExam)[:6]
    suspendend = str(TotalSuspended)[:6]
    death = str(TotalDeath)[:6]
    vacation = str(TotalVacation)[:6]
    certificate = str(TotalCertificate)[:6]
    absence = str(TotalAbsence)[:6]
    exame = str(TotalExam)[:6]
    training = str(TotalTraining)[:6]
    off = str(TotalOff)[:6]
    synergy = str(TotalSynergy)[:6]
    license = str(TotalLicense)[:6]
    away = str(TotalAway)[:6]
    covid = str(TotalCovid)[:6]
    transferred = str(TotalTransferred)[:6]
    dayoff = str(TotalDayOff)[:6]
    declaration = str(TotalDeclaration)[:6]

    connection = Connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Presenteismo ('presenteismo', 'exame', 'suspensao', 'falecimento', 'ferias', 'atestado', 'falta', 'treinamento', 'desligado', 'sinergia', 'licenca', 'afastado', 'covid', 'transferido', 'folga', 'area', 'turno', 'gestor', 'quantidade', 'declaracao') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (
        f'{Presenteeism}', f'{exame}%', f'{suspendend}%', f'{death}%', f'{vacation}%', f'{certificate}%', f'{absence}%',
        f'{training}%', f'{off}%', f'{synergy}%', f'{license}%', f'{away}%', f'{covid}%', f'{transferred}%',
        f'{dayoff}%', f'{ttarea.capitalize()}', 'Todos', 'Todos', f'{GrandTotal}', f'{declaration}%'))
    connection.commit()
    connection.close()
















