import speech_recognition as sr
import os
record = sr.Recognizer()
microphone = sr.Microphone()

def runProgramm(text):
    if str(text) == "photoshop":
        os.system("start C://users/user/Desktop/photoshop.lnk")
    if str(text) == "google":
        os.system("start C://users/user/Desktop/google.lnk")

try:
    while True:
        with microphone as source:
            record.adjust_for_ambient_noise(source)
            audio = record.listen(source)
            result=record.recognize_google(audio,language="ru_RU")
            result = result.lower()
            print(format(result))
            runProgramm(format(result))
except sr.UnknownValueError:
    print('Сервис google не отвечает')
