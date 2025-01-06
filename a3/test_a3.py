from city_weather import CityWeather
from main import extract_data


def test_extract_data_valid():
    weather = 'Bamberg: 🌤️ 🌡️5°C ↑ 10km/h'

    result = extract_data(weather)

    assert isinstance(result, CityWeather)
    assert result.city == 'Bamberg'
    assert result.icon == '🌤️'
    assert result.temperature == 5
    assert result.wind == 10


def test_extract_data_with_arrows():
    weather = 'Bamberg: 🌤️ 🌡️5°C ↑↑ 10km/h'

    result = extract_data(weather)

    assert result.city == 'Bamberg'
    assert result.icon == '🌤️'
    assert result.temperature == 5
    assert result.wind == 10
