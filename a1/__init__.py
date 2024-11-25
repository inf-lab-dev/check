import check50
import check50.c

CITIES = {
    'Phoenix': 107,
    'Las Vegas': 105,
    'Austin': 97,
    'Miami': 97,
    'Denver': 90,
    'Chicago': 85,
    'New York': 85,
    'Los Angeles': 82,
    'Boston': 82,
    'San Francisco': 66
}


@check50.check()
def exists():
    check50.exists('temperature.c')


@check50.check(exists)
def compiles():
    check50.c.compile('temperature.c', lcs50=True)


@check50.check(compiles)
def prints_cities():
    run = check50.run('./temperature')

    stdout = run.stdout()
    exit = run.exit()

    if exit != 0:
        raise check50.Failure(f'Expected exit code "0", but got "{exit}"')

    for city, temperature in CITIES.items():
        if not f'{city}: {temperature}\n' in stdout:
            raise check50.Failure(f'Expected city "{city}" to be printed with temperature "{
                                  temperature}"', help='Did you forget to add it?')
