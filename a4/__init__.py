import check50

a2 = check50.import_checks('../a2')
a3 = check50.import_checks('../a3')
from a3 import extract_data_valid
from a2 import fetch_weather_valid, fetch_weather_http_error, fetch_weather_exception

@check50.check()
def exists():
    """city_weather.py and main.py exist"""
    check50.exists('city_weather.py')
    check50.exists('main.py')
    
    check50.include('../a2/test_a2.py')
    check50.include('../a3/test_a3.py')
    check50.include('test_a4.py')


@check50.check(exists)
def main_valid():
    """main calls the implemented functions"""
    check50.run('pytest test_a4.py -k "test_main"').exit(0)
