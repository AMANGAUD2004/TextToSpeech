from NetHyTech_STT import listen
from TextToSpeech import text_to_speech
import threading
import time

def check():
    output_text = ""
    while True:
        try:
            with open("input.text",'r') as file:
                input_text = file.read().lower().strip()
                if input_text != output_text:
                    output_text = input_text
                    if output_text == input_text:
                        text_to_speech.speak(output_text)

        except Exception as e:
            pass
t1 = threading.Thread(target=listen)
t2 = threading.Thread(target=check)
t1.start()
t2.start()
t1.join()
t2.join()