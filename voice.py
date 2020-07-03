import speech_recognition as sr
from time import ctime
import webbrowser
import time
import  playsound
import  os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            allu_speek(ask)
        audio = r.listen(source)
        voice_data = ' '
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            allu_speek('Sorry , i did not get that')
        except sr.RequestError:
            allu_speek('Sorry, My speech Service is down')
        return voice_data

def allu_speek(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def respond(voice_data):
    if 'what is your name' in voice_data:
        allu_speek('My name is Allu')
    if 'who is your father' in voice_data:
        allu_speek('Technically speaking python code')
    if 'time please' in voice_data:
        allu_speek(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search ?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        allu_speek('Here is what i found for' + search)
    if 'find location' in voice_data:
        location = record_audio('what location you want ?')
        url = 'https://www.google.com/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        allu_speek('Here is the location of' + location)
    if 'go to paint' in voice_data:
        print('ok')
        allu_speek('oping paint')
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Paint.lnk')

    if 'back to home' in voice_data:
        allu_speek('OK have a nice day')
        exit()

time.sleep(1)
allu_speek('How can i Help you ...')
while 1:
    voice_data = record_audio()
    respond(voice_data)

