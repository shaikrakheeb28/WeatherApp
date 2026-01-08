# weather_app.py

import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }
            return weather
        elif response.status_code == 404:
            return {"error": "City not found"}
        else:
            return {"error": "Failed to retrieve data"}

def main():
    print("=== Weather App ===")
    api_key = input("Enter your OpenWeatherMap API Key: ")
    city = input("Enter city name: ")

    app = WeatherApp(api_key)
    result = app.get_weather(city)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"City: {result['city']}")
        print(f"Temperature: {result['temperature']}°C")
        print(f"Description: {result['description']}")
        print(f"Humidity: {result['humidity']}%")

if __name__ == "__main__":
    main()
