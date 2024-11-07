import pandas as pd

def loadDataFromCSV(ruta, columnas):
    """
    Obtener datos almacenados en un archivo csv

    :param ruta: (str) Ruta y nombre del archivo.
    :param columnas: (list) Lista con las columnas a recuperar (Ej. [0,1,2] o ['id', 'url'])
    :return:
    """
    datos = pd.read_csv(ruta, usecols=columnas)
    return datos

def saveDataToCSV(data, ruta):
    """
    Guarda la información en el archivo especificado.
    Si el archivo ya existe, solo agrega la información al final.
    Cuando la informacion tiene comas, se guarda entre comoillas ""

    :param data: (str) Informacion a almacenar
    :param ruta: (str) Ruta con nombre del archivo donde se va a almacenar la informacion
    :return:
    """
    # Convertir data a DataFrame
    df = pd.DataFrame(data)
    df.to_csv(ruta, index=False)