import check50


@check50.check()
def exists():
    """filter.py exists"""
    check50.exists('filter.py')
    
    check50.include('test_a5.py')


@check50.check(exists)
def temp_range_filter_init():
    """TempRangeFilter's init method works correctly"""
    check50.run('pytest test_a5.py -k "test_temp_range_filter_init"').exit(0)


@check50.check(exists)
def temp_range_filter_within_range():
    """TempRangeFilter's evaluate method passes values within the range"""
    check50.run(
        'pytest test_a5.py -k "test_temp_range_filter_within_range"').exit(0)


@check50.check(exists)
def temp_range_filter_below_range():
    """TempRangeFilter's evaluate method rejects values below the range"""
    check50.run(
        'pytest test_a5.py -k "test_temp_range_filter_below_range"').exit(0)


@check50.check(exists)
def temp_range_filter_above_range():
    """TempRangeFilter's evaluate method rejects values above the range"""
    check50.run(
        'pytest test_a5.py -k "test_temp_range_filter_above_range"').exit(0)
