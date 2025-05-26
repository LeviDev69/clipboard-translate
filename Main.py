import pyperclip
from deep_translator import GoogleTranslator
from time import sleep
from plyer import notification
try:
    last_clip = ""
    print("Translator active")
    while True:
        clip = pyperclip.paste()
        stripped_clip = clip.strip()
        if stripped_clip != last_clip and stripped_clip != "":
            last_clip = stripped_clip
            translated = GoogleTranslator(source='auto', target='en').translate(stripped_clip)
            notification.notify(
                title="Translation:",
                message=translated,
                app_name="Clipboard Translator",
                timeout=5
            )
        else:
            pass
        sleep(1)
except KeyboardInterrupt:
    print("Stopped by user exiting translator")
except Exception as e:
    print(f"[!]Error: {e}")
