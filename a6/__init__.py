import check50

a2 = check50.import_checks('../a2')
a3 = check50.import_checks('../a3')
a4 = check50.import_checks('../a4')
a5 = check50.import_checks('../a5')
from a5 import temp_range_filter_init, temp_range_filter_within_range, temp_range_filter_below_range, temp_range_filter_above_range
from a4 import main_valid
from a3 import extract_data_valid, extract_data_with_arrows
from a2 import fetch_weather_valid, fetch_weather_http_error, fetch_weather_exception

@check50.check()
def exists():
    """city_weather.py, main.py and filter.py exist"""
    check50.exists('city_weather.py')
    check50.exists('filter.py')
    check50.exists('main.py')

    check50.include('../a2/test_a2.py')
    check50.include('../a3/test_a3.py')
    check50.include('../a4/test_a4.py')
    check50.include('../a5/test_a5.py')
    check50.include('test_a6.py')


@check50.check(exists)
def main_valid():
    """main calls the implemented functions"""
    check50.run('pytest test_a6.py -k "test_main"').exit(0)
