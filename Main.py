#import libraries
import pyperclip
from deep_translator import GoogleTranslator
from time import sleep
from plyer import notification
from datetime import datetime

#make a log function
def log(original, translated):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {original} → {translated}\n")

#use try to make errors look cleaner and add the ability to exit
try:
    last_clip = ""
    print("Translator active")
    while True:
        clip = pyperclip.paste()
        stripped_clip = clip.strip()

        #make sure the clipboard is new and not blank for porformance
        if stripped_clip != last_clip and stripped_clip != "":
            last_clip = stripped_clip
            #translate
            translated = GoogleTranslator(source='auto', target='en').translate(stripped_clip)
            #print translation output
            print(f"Translated:\n{translated}")
            #create notification
            notification.notify(
                title=f"Translation:",
                message=translated,
                app_name="Clipboard Translator",
                timeout=5
            )
            log(clip, translated)
        else:
            pass
        sleep(1)
#makes ^c quit and tell the user
except KeyboardInterrupt:
    print("Stopped by user | exiting translator")
#error handeling
except Exception as e:
    print(f"[!]Error: {e}")