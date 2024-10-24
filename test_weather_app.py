import pytest
import requests
from app import get_weather_data

def test_weather_api():
    city = "Delhi"
    weather_data = get_weather_data(city)
    assert weather_data is not None
    assert "avg_temp" in weather_data
    assert "max_temp" in weather_data
    assert "min_temp" in weather_data

@pytest.mark.parametrize("city", ["Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"])
def test_multiple_cities_weather_api(city):
    weather_data = get_weather_data(city)
    assert weather_data is not None
    assert "avg_temp" in weather_data
    assert "max_temp" in weather_data
    assert "min_temp" in weather_data
