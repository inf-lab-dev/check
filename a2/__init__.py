import check50
import check50.c

a1 = check50.import_checks('../a1')
from a1 import exists, compiles, exits_with_zero, prints_cities

CITIES = {
    'Phoenix': 107,
    'Las Vegas': 105,
    'Austin': 97,
    'Miami': 97,
    'Denver': 90,
    'Chicago': 85,
    'New York': 85,
    'Boston': 82,
    'Los Angeles': 82,
    'San Francisco': 66
}


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
    print(printed_cities.values())
    print(sorted(CITIES.values(), reverse=True))
    if printed_cities.values() != sorted(CITIES.values(), reverse=True):
        raise check50.Failure('Temperatures are not sorted in descending order',
                              help='Ensure you sort the cities by temperature in descending order.')

    run.exit(0)
