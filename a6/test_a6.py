from unittest.mock import patch
from main import main, CityWeather


@patch('weather.fetch_weather')
@patch('weather.extract_data')
@patch('weather.TempRangeFilter')
def test_main(mock_temp_range_filter, mock_extract_data, mock_fetch_weather, capfd):
    mock_fetch_weather.side_effect = [
        'Bamberg: ⛅️  🌡️+25°C 🌬️↑10km/h',
        'Paris: 🌨  🌡️+18°C 🌬️→29km/h',
        'New York: ⛅️  🌡️+30°C 🌬️↗9km/h',
    ]

    mock_extract_data.side_effect = lambda weather: {
        'Bamberg: ⛅️  🌡️+25°C 🌬️↑10km/h': CityWeather('Bamberg', '🌤️', 25, 10),
        'Paris: 🌨  🌡️+18°C 🌬️→29km/h': CityWeather('Paris', '🌤️', 18, 29),
        'New York: ⛅️  🌡️+30°C 🌬️↗9km/h': CityWeather('New York', '🌤️', 30, 9),
    }[weather]

    filter_instance = mock_temp_range_filter.return_value
    filter_instance.evaluate.side_effect = lambda city_weather: 20 <= city_weather.temperature <= 25

    main()

    captured = capfd.readouterr()

    assert 'Bamberg matches the filter criteria!' in captured.out
    assert 'Paris does not match the filter criteria!' in captured.out
    assert 'New York does not match the filter criteria!' in captured.out
