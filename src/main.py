import os
from recoleccion.Transcriber import Transcriber
from recoleccion.downloader import downloadTikTok
from recoleccion.manageData import loadDataFromCSV, saveDataToCSV

def downloadAndTranscribe(urls, ruta_descarga, transcriber, ruta_transcripciones):
    data = []
    eliminados = 0
    fallidos = 0
    for url in urls:
        #1. Descargar video
        nombre_archivo = downloadTikTok(url, ruta_descarga)
        if not nombre_archivo: # No se pudo descargar el video
            print("No se ha logrado descargar el video: {url}")
            fallidos += 1
            continue
        print(f"Archivo descargado: {nombre_archivo}")

        #2. Transcribir video
        ruta_archivo = os.path.join(ruta_descarga, nombre_archivo)
        lang, text = transcriber.transcribe(ruta_archivo)
        data.append({"lang": lang, "text": text}) # Agregar transcripcion a la lista
        print(f"Archivo transcrito: {ruta_archivo}")
        #3. Eliminar video
        try:
            os.remove(ruta_archivo)
            eliminados += 1
            print(f"Video eliminado {ruta_archivo}")
        except FileNotFoundError:
            print(f"No se ha encontrado el archivo {ruta_archivo} para su eliminacion")
        except PermissionError:
            print(f"No tienes permisos para eliminar el archivo {ruta_archivo}")

    # Guardar transcripciones en archivo csv
    saveDataToCSV(data, ruta_transcripciones)
    print(f"[Transcripciones guardadas correctamente: {len(data)}/{len(urls)}]")
    print(f"[Archivos eliminados correctamente: {eliminados}/{len(urls)}]")
    print(f"[No se ha logrado descargar {fallidos} videos]")


if __name__ == '__main__':
    # Cargar datos extraidos
    ruta_actual = os.path.join(os.getcwd(), "recoleccion")
    archivo_datos = os.path.join(ruta_actual, os.path.join("datos_extraidos", "data.csv"))
    data = loadDataFromCSV(archivo_datos, ['url']) # devuelve datos tabulados'

    # Cargar modelo
    modelo = 'base'
    device = 'cpu'
    transcriber = Transcriber(modelo, device)

    # Decargar videos y guardar transcripcion
    ruta_descarga_videos = os.path.join(ruta_actual, "videos")
    ruta_transcripciones = os.path.join(ruta_actual, "transcripciones.csv")
    downloadAndTranscribe(data['url'], ruta_descarga_videos, transcriber, ruta_transcripciones) # obtener solo la información de la columna url