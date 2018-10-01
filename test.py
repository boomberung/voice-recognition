import requests
from bs4 import BeautifulSoup

UNDEFINED_STRING='undefined'
KEY = 'f4e6b918-0f5d-4406-a838-effba8c97f60'
#UUID можно любой (01ae13cb744628b58fb536d496daa1e6)
UUID='01ae13cb744628b58fb536d496daa1e6'


url = 'https://asr.yandex.net/asr_xml?key=' + KEY + '&uuid=' + UUID + '&topic=queries&lang=ru-RU'
headers = {"Content-Type": 'audio/x-wav'}
#файл распознования
data = open ('output.wav', 'rb')

response = requests.post(url, headers=headers, data=data)

soup = BeautifulSoup(response.text, 'html.parser')

#soup.variant
result=UNDEFINED_STRING
answers=soup.findAll('variant')
if(len(answers)>0):
    result=answers[0].text
    print(result)
else:
    print(UNDEFINED_STRING)
