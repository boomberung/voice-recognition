import pyaudio
import wave
import requests
from bs4 import BeautifulSoup
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

UNDEFINED_STRING='undefined'
KEY = 'f4e6b918-0f5d-4406-a838-effba8c97f60'
#UUID можно любой (01ae13cb744628b58fb536d496daa1e6)
UUID='01ae13cb744628b58fb536d496daa1e6'
result=UNDEFINED_STRING

def recording():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def recognize():
    global result
    url = 'https://asr.yandex.net/asr_xml?key=' + KEY + '&uuid=' + UUID + '&topic=queries&lang=ru-RU'
    headers = {"Content-Type": 'audio/x-wav'}
    #файл распознования
    data = open ('output.wav', 'rb')

    response = requests.post(url, headers=headers, data=data)

    soup = BeautifulSoup(response.text, 'html.parser')

    #soup.variant
    answers=soup.findAll('variant')
    if(len(answers)>0):
        result=answers[0].text
        print(result)
    else:
        print(UNDEFINED_STRING)

def action():
    if result == 'открыть телегу':
        os.startfile(r'"C:\Users\work\AppData\Roaming\Telegram Desktop\Telegram.exe"')

recording()
recognize()
#action()
