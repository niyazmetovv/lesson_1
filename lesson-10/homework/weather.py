import requests
import json

#My data
API_KEY = "cb77f2e7599c26ba5a7057dbf4009af0"
CITY = input("Enter City: ")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"



#Fixed
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

#Request
response = requests.get(BASE_URL, params=params)
data = response.json()
# print(json.dumps(data, indent=4))



#Output
if response.status_code == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_desc = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_desc.capitalize()}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error:", data.get("message", "Failed to retrieve data"))
