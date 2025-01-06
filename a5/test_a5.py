from city_weather import CityWeather
from filter import TempRangeFilter


def test_temp_range_filter_init():
    filter = TempRangeFilter(min_temp=10, max_temp=20)

    assert filter.min_temp == 10
    assert filter.max_temp == 20


def test_temp_range_filter_within_range():
    city_weather = CityWeather('Bamberg', '🌤️', 15, 10)
    filter = TempRangeFilter(min_temp=10, max_temp=20)

    assert filter.evaluate(city_weather) is True


def test_temp_range_filter_below_range():
    city_weather = CityWeather('Bamberg', '🌤️', 5, 10)
    filter = TempRangeFilter(min_temp=10, max_temp=20)

    assert filter.evaluate(city_weather) is False


def test_temp_range_filter_above_range():
    city_weather = CityWeather('Bamberg', '🌤️', 25, 10)
    filter = TempRangeFilter(min_temp=10, max_temp=20)

    assert filter.evaluate(city_weather) is False
