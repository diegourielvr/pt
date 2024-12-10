import os
import unittest
from src.recoleccion.downloader import downloadTikTok

class DownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.ruta_descarga = os.path.join(os.getcwd(), 'recoleccion/archivos')

    def test_download_video(self):
        url = 'https://www.tiktok.com/@larepublica.pe/video/7434179049892711735'
        self.assertEqual(downloadTikTok(url, self.ruta_descarga), '7434179049892711735.mp4')

    def test_download_sin_ruta(self):
        url = 'https://www.tiktok.com/@cnnee/video/7434178277570317624'
        self.assertEqual(downloadTikTok(url), '7434178277570317624.mp4')

    def test_download_id_inexistente(self):
        url = 'https://www.tiktok.com/@larepublica.pe/video/7434179049892711730'
        self.assertIsNone(downloadTikTok(url))

    def test_download_sin_url(self):
        url = ''
        self.assertIsNone(downloadTikTok(url))
