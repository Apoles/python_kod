import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
print("""
 ______________________________________________________________________________
|                                                                              |
|                          3Kom SuperHack II Logon                             |
|______________________________________________________________________________|
|                                                                              |
|                                                                              |
|                                                                              |
|                 User Name:          [   Apoles      ]                        |
|                                                                              |
|                 Password:           [   Gümüş       ]                        |
|                                                                              |
|                                                                              |
|                                                                              |
|                                   [ OK ]                                     |
|______________________________________________________________________________|
|                                                                              |
|                                                       https://Apoles.com     |
|______________________________________________________________________________|
""")



r=sr.Recognizer()

def ses_kaydı(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source) 
        voice=''
        try:
            voice=r.recognize_google(audio,language="tr-TR ")    
        except sr.UnknownValueError:
            print("============================")
            time.sleep(0.5)
            print("VOİCE DONT GET UNDERSTAND ")
        except sr.RequestError:
            print("SYSTEM FOUNT ERROR")
        return voice

def dönüş(voice):
    if 'nasılsın' in voice:
        speak("I am good how you doin?")
    if 'saat kaç' in voice:
        #speak(datetime.datetime.now())
        speak(datetime.now().strftime('%H:%M:%S:'))
    if 'arama yap' in voice:
        search=ses_kaydı("what do you want to search")
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak("what I found for "+search)
    if 'tamamdır' in voice:
        speak("See you later")
        exit()
    if ' mal insanı kimdir' in voice:
        speak("Abdussametdir")
def speak(string):
    tts=gTTS(string)#,lang='tr')
    rand=random.randint(1,10000) 
    file='audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


speak("May I help you?")
time.sleep(1)
while 1:
    voice=ses_kaydı()
    print("============================")
    time.sleep(0.5)
    print(voice)
    time.sleep(0.5)
    print("============================")
    dönüş(voice)
