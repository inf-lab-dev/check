from unittest.mock import patch
from main import main


@patch('main.fetch_weather')
def test_main(mock_fetch_weather, capfd):
    mock_fetch_weather.side_effect = [
        'Bamberg: ⛅️  🌡️+25°C 🌬️↑10km/h',
        'Paris: 🌨  🌡️+18°C 🌬️→29km/h',
        'New York: ⛅️  🌡️+30°C 🌬️↗9km/h',
    ]

    with patch('main.CITIES_LIST', ['Bamberg', 'Paris', 'New York']):
        main()

    captured = capfd.readouterr()

    assert 'Bamberg matches the filter criteria!' in captured.out
    assert 'Paris does not match the filter criteria!' in captured.out
    assert 'New York does not match the filter criteria!' in captured.out
