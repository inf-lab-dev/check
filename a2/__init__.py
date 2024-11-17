import check50
import check50.c

a1 = check50.import_checks('../a1')
from a1 import exists, compiles, prints_header, empty_input

@check50.check(compiles)
def single_item():
    (check50.run('./snackbar')
     .stdin('Pizza')
     .stdin('')
     .stdout('\nThe order costs 8.91 €', regex=False)
     .exit(0))


@check50.check(compiles)
def multiple_items():
    (check50.run('./snackbar')
        .stdin('Burger')
        .stdin('Fries')
        .stdin('')
        .stdout('\nThe order costs 10.69 €', regex=False)
        .exit(0))


@check50.check(compiles)
def invalid_item():
    (check50.run('./snackbar')
        .stdin('Pasta')
        .stdout('The provided dish wasn\'t found', regex=False)
        .stdin('')
        .stdout('\nThe order costs 0.00 €', regex=False)
        .exit(0))


@check50.check(compiles)
def mixed_items():
    (check50.run('./snackbar')
        .stdin('Burger')
        .stdin('Pasta')
        .stdout('The provided dish wasn\'t found', regex=False)
        .stdin('Soda')
        .stdin('')
        .stdout('\nThe order costs 9.50 €', regex=False)
        .exit(0))


@check50.check(compiles)
def case_insensitive():
    (check50.run('./snackbar')
        .stdin('burger')
        .stdin('PIZZA')
        .stdin('sALad')
        .stdin('')
        .stdout('\nThe order costs 21.98 €', regex=False)
        .exit(0))
