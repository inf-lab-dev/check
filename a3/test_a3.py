from city_weather import CityWeather
from main import extract_data

ARROWS = ['↑', '↗', '→', '↘', '↓', '↙', '←', '↖']


def test_extract_data_valid():
    for arrow in ARROWS:
        weather = f'Bamberg: ⛅️  🌡️+5°C 🌬️{arrow}10km/h'

        result = extract_data(weather)

        assert isinstance(result, CityWeather)
        assert result.city_name == 'Bamberg'
        assert result.condition == '⛅️'
        assert result.temperature == 5
        assert result.wind == 10
