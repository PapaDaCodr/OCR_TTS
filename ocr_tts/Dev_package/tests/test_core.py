import unittest
from ocr_tts.Dev_package.ocr_tts import image_to_text, text_to_audio, image_to_audio
from PIL import Image
import os


class TestOCRTTS(unittest.TestCase):
    def test_image_to_text(self):
        text = image_to_text('tests/test_image.png')
        self.assertIn("expected text", text)

    def test_text_to_audio(self):
        text_to_audio("Hello, world!", 'tests/output.mp3')
        self.assertTrue(os.path.exists('tests/output.mp3'))
        os.remove('tests/output.mp3')

    def test_image_to_audio(self):
        image_to_audio('tests/test_image.png', 'tests/output.mp3')
        self.assertTrue(os.path.exists('tests/output.mp3'))
        os.remove('tests/output.mp3')


if __name__ == '__main__':
    unittest.main()
