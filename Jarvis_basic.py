import pyttsx3
import speech_recognition as sr
from PyInstaller.utils.hooks import collect_submodules

hidden_imports=collect_submodules('pyttsx3')
hiddenimports=hidden_imports


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio,language='en-in')
        print('Did you say : {}'.format(query))
    except Exception :
        print('Say it Again')
        query='None'
    return query 
