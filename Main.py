import pyperclip
from deep_translator import GoogleTranslator
from time import sleep
from plyer import notification

last_clip = ""

while True:
    clip = pyperclip.paste()
    stripped_clip = clip.strip()
    if stripped_clip != last_clip and stripped_clip != "":
        last_clip = stripped_clip
        translated = GoogleTranslator(source='auto', target='en').translate(stripped_clip)
        notification.notify(
            title="Translation:",
            message=translated,
            timeout=5
        )
    else:
        pass
    sleep(1)
