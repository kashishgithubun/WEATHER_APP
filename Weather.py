import requests

API_KEY = "c7ec4c9f534bb59abe01065ec23da2be"  # replace with your actual key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
else:
    print("City not found or API error")
