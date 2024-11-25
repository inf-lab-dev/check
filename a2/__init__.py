from a1 import CITIES, exists, compiles, exits_with_zero, prints_cities
import check50
import check50.c

a1 = check50.import_checks('../a1')


@check50.check(prints_cities)
def prints_sorted_cities():
    run = check50.run('./temperature')
    stdout = run.stdout()

    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    printed_cities = {}

    for line in lines:
        if ': ' in line:
            city, temperature = line.rsplit(': ', 1)

            try:
                printed_cities[city] = int(temperature)
            except ValueError:
                continue

    if list(printed_cities.values()) != sorted(CITIES.values(), reverse=True):
        raise check50.Failure(
            'Temperatures are not sorted in descending order')


@check50.check(prints_sorted_cities)
def prints_hottest_city():
    (check50.run('./temperature')
     .stdout('The highest temperature in July is in Austin.')
     .exit(0))
