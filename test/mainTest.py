import unittest
from recoleccion.DownloaderTestCase import DownloaderTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DownloaderTestCase('test_download_video'))
    suite.addTest(DownloaderTestCase('test_download_sin_ruta'))
    suite.addTest(DownloaderTestCase('test_download_id_inexistente'))
    suite.addTest(DownloaderTestCase('test_download_sin_url'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
