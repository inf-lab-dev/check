from unittest.mock import patch
from city_weather import CityWeather
from main import main


@patch('weather.fetch_weather')
@patch('weather.extract_data')
def test_main(mock_extract_data, mock_fetch_weather):
    mock_fetch_weather.return_value = 'Bamberg: 🌤️ 🌡️5°C ↑ 10km/h'
    mock_extract_data.side_effect = lambda weather: CityWeather(
        'Bamberg', '🌤️', 5, 10)

    with patch('weather.CITIES_LIST', ['Bamberg']):
        main()

    mock_fetch_weather.assert_called_once_with('Bamberg')
    mock_extract_data.assert_called_once_with('Bamberg: 🌤️ 🌡️5°C ↑ 10km/h')
