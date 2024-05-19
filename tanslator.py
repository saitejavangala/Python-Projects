'''
from deep_translator import GoogleTranslator
t=GoogleTranslator(
    source="auto",
    target="bn",
    sound="Voice"

)
r=t.translate("how are you?")
print(r) '''

from deep_translator import GoogleTranslator
from gtts import gTTS

def translate_and_speak(text, source="auto", target="hi"):
    

    translator = GoogleTranslator(source=source, target=target)
    translated_text = translator.translate(text)

    
    speaker = gTTS(text=translated_text, lang=target)

   
    speaker.save("translation.mp3")

   
    import os
    os.system("start translation.mp3")  


text = input("enter: ")
translate_and_speak(text)

