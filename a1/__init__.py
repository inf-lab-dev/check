import check50
import check50.c


@check50.check()
def exists():
    check50.exists('snackbar.c')


@check50.check(exists)
def compiles():
    check50.c.compile('snackbar.c', lcs50=True)


@check50.check(compiles)
def prints_header():
    (check50.run('./snackbar')
     .stdout('Welcome to our Snackbar!\n', regex=False)
     .stdout('  Choose your dishes, press Enter when done.\n', regex=False)
     .stdout('\n', regex=False)
     .stdin('')
     .exit(0))


@check50.check(compiles)
def single_dish():
    (check50.run('./snackbar')
     .stdin('Pizza')
     .stdin('')

     .stdout('\nThe order costs 7.49 €', regex=False)
     .exit(0))


@check50.check(compiles)
def multiple_items():
    (check50.run('./snackbar')
     .stdin('Burger')
     .stdin('Fries')
     .stdin('')
     .stdout('\nThe order costs 8.98 €', regex=False)
     .exit(0))


@check50.check(compiles)
def invalid_item():
    (check50.run('./snackbar')
     .stdin('iPhone 16 Pro')  # we're not in an Apple(TM) store :D
     .stdin('')
     .stdout('The provided dish wasn\'t found', regex=False)
     .stdout('\nThe order costs 0.00 €', regex=False)
     .exit(0))


@check50.check(compiles)
def mixed_items():
    (check50.run('./snackbar')
     .stdin('Burger')
     .stdin('iPhone 16 Pro')
     .stdout('The provided dish wasn\'t found', regex=False)
     .stdin('Soda')
     .stdin('')
     .stdout('\nThe order costs 7.98 €', regex=False)
     .exit(0))


@check50.check(compiles)
def empty_input():
    (check50.run('./snackbar')
     .stdin('')
     .stdout('\nThe order costs 0.00 €', regex=False)
     .exit(0))


@check50.check(compiles)
def case_insensitive():
    (check50.run('./snackbar')
     .stdin('burger')
     .stdin('PIZZA')
     .stdin('sALad')
     .stdin('')
     .stdout('\nThe order costs 18.47 €', regex=False)
     .exit(0))
