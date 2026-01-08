# test_weather_app.py

import unittest
from unittest.mock import patch
from weather_app import WeatherApp

class TestWeatherApp(unittest.TestCase):
    @patch("weather_app.requests.get")
    def test_get_weather_success(self, mock_get):
        mock_response = {
            "name": "London",
            "main": {"temp": 15, "humidity": 70},
            "weather": [{"description": "clear sky"}]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        app = WeatherApp("fake_api_key")
        result = app.get_weather("London")
        self.assertEqual(result["city"], "London")
        self.assertEqual(result["temperature"], 15)
        self.assertEqual(result["description"], "clear sky")
        self.assertEqual(result["humidity"], 70)

    @patch("weather_app.requests.get")
    def test_city_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        app = WeatherApp("fake_api_key")
        result = app.get_weather("FakeCity")
        self.assertEqual(result["error"], "City not found")

    @patch("weather_app.requests.get")
    def test_api_failure(self, mock_get):
        mock_get.return_value.status_code = 500
        app = WeatherApp("fake_api_key")
        result = app.get_weather("AnyCity")
        self.assertEqual(result["error"], "Failed to retrieve data")

if __name__ == "__main__":
    unittest.main()
