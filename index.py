import requests
import json

API_KEY = "API_KEY 입력해주세요"
LAT = '37.5665'
LON = '126.9780'
URL = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=kr"

def seoul_weather():
    response = requests.get(URL)
    if  response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        
        print(f"서울의 현재 온도: {temp}")
        print(f"체감 온도: {feels_like}")
        print(f"날씨 상태: {weather} - {description}")
    else:
        print("날씨를 불러올수 없습니다. API KEY 를 잘 입력했는지 다시한번 확인해주세요.")


seoul_weather()