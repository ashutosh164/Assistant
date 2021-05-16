import speech_recognition as voice
import playsound
from gtts import gTTS


def speech(voice_data):
    print('Speaking....')
    if 'pihu ' in voice_data.lower():
        audio_string = 'yes brother, how may i help you'
    elif 'hello' in voice_data.lower():
        audio_string = 'yes how may i help you'
    else:
        audio_string = 'sorry i did not get that'
    tts = gTTS(text=audio_string,lang="en")
    audio_file = 'audio.mp3 '
    tts.save(audio_file)
    playsound.playsound(audio_file)


rec = voice.Recognizer()


def listen():
    with voice.Microphone(device_index=1) as source:
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
        except :
            print('i did not get that')

    print(f'you said: {voice_data}')
    speech(voice_data)


bot = listen()

