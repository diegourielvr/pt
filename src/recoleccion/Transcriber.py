import whisper
import os

class Transcriber:
    def __init__(self, modelo='tiny', device='cpu'):
        self.model = whisper.load_model(name=modelo, device=device) # tiny | base | small | medium | large

    def transcribe(self, ruta):
        """
        Trancribe un archivo de  audio/video a texto

        :param ruta: (str) Ruta del archivo a transcribir, incluyendo la extension del archivo.
        :return: Devuelve el lenguaje y el texto del archivo, si no existe el rchivo devuelve None
        """
        if not os.path.exists((ruta)):
            print(f"No existe la ruta: {ruta}")
            return None
        result = self.model.transcribe(ruta)
        return result['language'], result['text']

    def transcribeGetAllInfo(self, ruta):
        """
        Trancribe un archivo de  audio/video a texto.

        :param ruta: (str) Ruta del archivo a transcribir, incluyendo la extension del archivo.
        :return: Devuelve toda la información extraida
        """
        ruta = ruta.strip()
        if ruta.endswith('/') or ruta.endswith("\\") or not ruta.endswith('.mp4'):
            print("La ruta debe ser un archivo y debe tener la extension mp4!")
            return None
        if not os.path.exists(ruta):
            print(f"La ruta es incorrecta: {ruta}")
            return None
        result = self.model.transcribe(ruta)
        return result

