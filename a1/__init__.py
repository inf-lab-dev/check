import check50
import check50.c

CITIES = {
    'Austin': 36,
    'Boston': 28,
    'Chicago': 29,
    'Denver': 32,
    'Las Vegas': 41,
    'Los Angeles': 28,
    'Miami': 36,
    'New York': 29,
    'Phoenix': 42,
    'San Francisco': 19
}


@check50.check()
def exists():
    check50.exists('temperature.c')


@check50.check(exists)
def compiles():
    check50.c.compile('temperature.c', lcs50=True)


@check50.check(compiles)
def exits_with_zero():
    check50.run('./temperature').exit(0)


@check50.check(exits_with_zero)
def prints_cities():
    run = check50.run('./temperature')
    stdout = run.stdout()

    for city, temperature in CITIES.items():
        if not f'{city}: {temperature}\n' in stdout:
            raise check50.Failure(f'Expected city "{city}" to be printed with temperature "{
                                  temperature}"', help='Did you forget to add it?')
