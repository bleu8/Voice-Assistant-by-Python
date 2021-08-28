from gtts import gTTS
import speech_recognition as sr
import os
from playsound import playsound
from datetime import datetime
import webbrowser


r=sr.Recognizer()

def spe(metn):
    tts=gTTS(text=metn,lang="tr",slow=False)
    tts.save("metn.mp3")
    os.system("metn.mp3")
    #playsound("metn.mp3")
    #os.remove("metn.mp3")



def rec():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr")
        except sr.UnknownValueError:
            print("seni duyamıyorum")
        return voice
    
def cev(voice):
    if "nasılsın" in voice:
        spe("iyidir sen nasılsın")
    elif "saat kaç" in  voice:
        spe(datetime.now().strftime("%H:%M:%S"))
    elif "arama yap":
        spe("ne arayacağız")
        search=rec()
        url="https://www.google.com/search?client=firefox-b-d&q="+search
        webbrowser.get().open(url)
        spe(search+"icin bulduklarım")
    elif "kapat" in voice:
        spe("bay bay")
        exit()
    


spe("sana  nasıl yardımcı olabilirim")
while(1):
    voice=rec()
    print(voice)
    cev(voice)
    







