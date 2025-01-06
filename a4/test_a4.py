from unittest.mock import patch
from main import main


@patch('main.fetch_weather')
def test_main(mock_fetch_weather):
    mock_fetch_weather.return_value = 'Bamberg: ⛅️  🌡️+5°C 🌬️↑10km/h'

    with patch('main.CITIES_LIST', ['Bamberg']):
        main()

    mock_fetch_weather.assert_called_once_with('Bamberg')
