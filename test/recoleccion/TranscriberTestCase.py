import unittest
import os
from src.recoleccion.Transcriber import Transcriber
from src.recoleccion.downloader import downloadTikTok

class TranscriberTestCase(unittest.TestCase):
    def setUp(self):
        self.ruta_archivos = os.path.join(os.getcwd(), "recoleccion/archivos")
        self.transcriber = Transcriber('tiny', 'cpu')
        urls = ['https://www.tiktok.com/@groberurbina/video/7224550100012436742',
                'https://www.tiktok.com/@politicomx/video/7434291773310029112',
                'https://www.tiktok.com/@le_giovaz/video/7431738707671108870',
                'https://www.tiktok.com/@elespanolcom/video/7434078874721406240',
                'https://www.tiktok.com/@mileicortos/video/7433968812971740421',
                'https://www.tiktok.com/@eluniversalmx/video/7434262846923410744',
                'https://www.tiktok.com/@andra.consulting/video/7211543347721260294']
        for url in urls:
            downloadTikTok(url, self.ruta_archivos)

    def transcribe_spanish(self):
        #url = 'https://www.tiktok.com/@groberurbina/video/7224550100012436742'
        archivo = '7224550100012436742.pm4'
        lang, text = self.transcriber.transcribe(os.path.join(self.ruta_archivos, archivo))
        self.assertEqual(lang, 'es')
        self.assertIsNotNone(text)

    def transribe_ingles(self):
        #url = 'https://www.tiktok.com/@politicomx/video/7434291773310029112'
        archivo = '7434291773310029112.mp4'
        lang, text = self.transcriber.transcribe(os.path.join(self.ruta_archivos, archivo))
        self.assertEqual(lang, 'en')
        self.assertIsNotNone(text)

    def transcribe_no_voice(self):
        #url = 'https://www.tiktok.com/@le_giovaz/video/7431738707671108870'
        archivo = '7431738707671108870.mp4'
        lang, text = self.transcriber.transcribe(os.path.join(self.ruta_archivos, archivo))
        self.assertIsNone(text)

    def transcribe_music(self):
        #url = 'https://www.tiktok.com/@elespanolcom/video/7434078874721406240'
        archivo = '7434078874721406240.mp4'

    def transcribe_voice_and_music_with_voice(self):
        #url = 'https://www.tiktok.com/@mileicortos/video/7433968812971740421'
        archivo = '7433968812971740421.mp4'

    def transcribe_voice_and_music_without_voice(self):
        #url = 'https://www.tiktok.com/@eluniversalmx/video/7434262846923410744'
        archivo = '7434262846923410744.mp4'

    def transcribe_multiple_voices(self):
        #url = 'https://www.tiktok.com/@andra.consulting/video/7211543347721260294'
        archivo = '7211543347721260294.mp4'

    def transcribe_invalid_type(self):
        archivo = 'myfile.pdf'

    def transcribe_file_not_found(self):
        archivo = 'myaudio.mp3'

