import requests
#This line gets input from the user and assigns it to the user_input variable
# This only works when the input is a string of a major city
user_input = input("What city are you interested in: ")

#This line assigns the API key to a varibale called api_key
#This is needed to run the requests.get in the next line
api_key = 'f1361d802e1df05b30a5a16b24e93965'

#This line sends a GET request to the OpenWeatherMap API and formats the user_input variable and 
# the api_key variable. 
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#These two lines index the json data from the weather_data variable and store weather conditions 
# in the weather varibale and the temperature in the temperature variable. 
# This involves indexing json files.
weather = weather_data.json()['weather'][0]['main']
temperature = weather_data.json()['main']['temp']

#This prints the weather conditions and temperature
print(weather, temperature)