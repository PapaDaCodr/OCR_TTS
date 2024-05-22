from PIL import Image
import pytesseract
from gtts import gTTS


def image_to_text(image_path):
    """
    Extract text from an image file.

    :param image_path: Path to the image file
    :return: Extracted text
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


def text_to_audio(text, audio_path):
    """
    Convert text to speech and save as an audio file.

    :param text: Text to convert
    :param audio_path: Path to save the audio file
    """
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)


def image_to_audio(image_path, audio_path):
    """
    Convert text from an image to speech and save as an audio file.

    :param image_path: Path to the image file
    :param audio_path: Path to save the audio file
    """
    text = image_to_text(image_path)
    text_to_audio(text, audio_path)
