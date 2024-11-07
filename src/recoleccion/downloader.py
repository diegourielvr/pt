import os
import yt_dlp

# Nota: TikTok solo permite descargar videos en formato mp4, si se requiere otro formato será necesario convertir de mp4 al nuevo formato
def downloadTikTok(url, ruta_descarga=None):
    """
    Descarga un video en la ruta y formato especificado.

    Si no existe la ruta entonces la crea.
    Si no se especifica una ruta entonces lo guarda en la ruta actual,
    Si no se especifica el formato entonces descarga el de mejor calidad,
    Por defecto los videos de TikTok están en formato mp4.
    El Id de un tiktok es gobal, no es unico de un usuario. Si el id existe y el user no entonces descarga el video correctamente

    :param url: (str) Url del audio o video.
    :param ruta_descarga: (str) Ruta donde será guardado el archivo. Default: os.getcwd()
    :param formato_descarga: Formato del archivo guardado 'mp3' | 'mp4' | 'wav'. Default: 'bestaudio/bestvideo/best'
    :return: (bool) Devuelve el Id del video, de lo contrario devuelve None
    """

    if not url:
        print("No se ha espepcificado una url")
        return None

    if not ruta_descarga:
        ruta_descarga = os.getcwd()

    ydl_opts = {
        'format': 'bestaudio/bestvideo/best',  # Orden de preferencia separado por '/'
        'outtmpl': f'{ruta_descarga}/%(id)s.%(ext)s',
    }
    return downloadDefault(url, ydl_opts)

def downloadDefault(url, opts):
    result = None
    with yt_dlp.YoutubeDL(opts) as ydl:
        try:
            #ydl.download(url) # Solo dscargar el video
            info = ydl.extract_info(url, download=True) # Descargar info + video
            result = f"{info.get('id')}.{info.get('ext')}"
        except yt_dlp.utils.DownloadError as e:
            print(f"Error al descargar el video {url}. Posiblemente el video ya no existe")
        except Exception as e:  # Capturar otras posibles excepciones
            print(f"Error: {str(e)}")
    return result