import speech_recognition as sr
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from  gtts import gTTS


r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speech(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speech('Sorry. I did not get that')
        except sr.RequestError:
            speech('Sorry, my speech services is down')
        return voice_data


def speech(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'hello' in voice_data:
        speech('My name is Alian')
    if 'ok' in voice_data:
        speech(ctime())
    if 'c' in voice_data:
        a = 'what do you want search for'
        search = record_audio(a)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        search('here is what i found for ' + search)
    if 'map' in voice_data:
        b = 'what is the location you want to looking for ?'
        location = record_audio(b)
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        location('here is the location of ' + location)
    if 'stop' in voice_data:
        speech('thank you have a good day')
        exit()


time.sleep(1)
speech('How can i help you?')
while 1:
    voice_data = record_audio()
    # print(voice_data)
    respond(voice_data)




