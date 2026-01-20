import requests

city_name =input("enter city name")
API_key ="db3b535ee303f3c82bc4239a9ed8bd8d"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"


response= requests.get(url)
if response.status_code == 200:
    data=response.json()
    print('Weather is',data['weather'][0]['description'])
    print('Current Temperature is',data['main']['temp'])
    print('Current Temperature feels like is',data['main']['feels_like'])
    print('humidity  feels like is',data['main']['humidity'])
if response.status_code != 200:
    print("Invalid city name or API issue")

    
