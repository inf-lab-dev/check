import check50


@check50.check()
def exists():
    """main.py exists"""
    check50.exists('main.py')

    check50.include('test_a2.py')


@check50.check(exists)
def fetch_weather_valid():
    """fetch_weather returns correct result from api"""
    check50.run('pytest test_a2.py -k "test_fetch_weather_valid"').exit(0)


@check50.check(exists)
def fetch_weather_http_error():
    """fetch_weather returns string describing http errors if any"""
    check50.run('pytest test_a2.py -k "test_fetch_weather_http_error"').exit(0)


@check50.check(exists)
def fetch_weather_exception():
    """fetch_weather returns string describing exceptions if any"""
    check50.run('pytest test_a2.py -k "test_fetch_weather_exception"').exit(0)
