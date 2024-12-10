import requests

user_input = input("What city are you interested in: ")

api_key = 'f1361d802e1df05b30a5a16b24e93965'

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temperature = weather_data.json()['main']['temp']

print(weather, temperature)