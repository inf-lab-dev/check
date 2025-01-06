from unittest.mock import patch
from main import fetch_weather


def test_fetch_weather_valid():
    response = 'Bamberg: 🌤️ +5°C'

    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = response

        result = fetch_weather('Bamberg')

        assert result == response


def test_fetch_weather_http_error():
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        result = fetch_weather('Hinterdupfingen')

        assert 'Error' in result
        assert '404' in result


def test_fetch_weather_exception():
    with patch('requests.get', side_effect=Exception('Connection error')):
        result = fetch_weather('Bamberg')

        assert 'Error: Connection error' in result
