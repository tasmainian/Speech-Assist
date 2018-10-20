from gtts import gTTS
import os
import keyboard

def Speak(sentence):
    tts = gTTS(text = sentence, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
