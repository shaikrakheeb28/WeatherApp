# Weather App (Console using API)

A Python console app that fetches real-time weather data using the OpenWeatherMap API.

## Features

- Get current temperature, humidity, and weather description by city name
- Handles invalid city names and API failures gracefully
- Includes unit tests with mocking

## Requirements

- Python 3.x
- `requests` library
- OpenWeatherMap API Key (Free at https://openweathermap.org/api)

## Steps to Run in PyCharm IDE

1. Open PyCharm IDE.
2. Click `File` > `Open` and select the `WeatherApp` directory.
3. Install dependencies using terminal:
   ```
   pip install requests
   ```
4. Run `weather_app.py` and enter your OpenWeatherMap API key and a city name.
5. To run tests, right-click `test_weather_app.py` and choose `Run`.

## Test Scenarios

- Successful API response for a valid city
- City not found error (404)
- API failure (500 or other)

## Author

Name: Sekhar Metla (www.harisystems.com)
