import check50
import check50.c

a3 = check50.import_checks('../a3')
from a3 import exists, compiles, prints_header, empty_input

@check50.check(compiles)
def single_item():
    (check50.run('./snackbar')
        .stdin('Pizza')
        .stdin('3')  # Requesting 3 Pizzas
        .stdin('')
        .stdout('\nThe order costs 26.75 €', regex=False)
        .exit(0))


@check50.check(compiles)
def multiple_items():
    (check50.run('./snackbar')
        .stdin('Burger')
        .stdin('2')  # Requesting 2 Burgers
        .stdin('Soda')
        .stdin('5')  # Requesting 5 Sodas
        .stdin('')
        .stdout('\nThe order costs 20.68 €', regex=False)
        .exit(0))


@check50.check(compiles)
def invalid_item():
    (check50.run('./snackbar')
        .stdin('Pasta')  # Invalid dish
        .stdin('2')
        .stdout('The provided dish wasn\'t found', regex=False)
        .stdin('')
        .stdout('\nThe order costs 0.00 €', regex=False)
        .exit(0))


@check50.check(compiles)
def out_of_stock():
    (check50.run('./snackbar')
        .stdin('Salad')
        .stdin('5')  # Exceeds available stock of 3
        .stdout('Not enough dishes available. 3 dishes were sold.', regex=False)
        .stdin('')
        .stdout('The order costs 17.81 €', regex=False)
        .exit(0))


@check50.check(compiles)
def mixed_items_with_stock():
    (check50.run('./snackbar')
        .stdin('Burger')
        .stdin('2')         # Valid order
        .stdin('Pasta')     # Invalid order
        .stdin('5')
        .stdout('The provided dish wasn\'t found', regex=False)
        .stdin('Soda')
        .stdin('20')        # Exceeds stock, only 16 available
        .stdout('Not enough dishes available. 16 dishes were sold.', regex=False)
        .stdin('Salad')
        .stdin('3')         # Valid order
        .stdin('')
        .stdout('\nThe order costs 55.24 €', regex=False)
        .exit(0))


@check50.check(compiles)
def invalid_amount():
    (check50.run('./snackbar')
        .stdin('Pizza')
        .stdin('0')     # Invalid quantity
        .stdin('-3')    # Invalid quantity
        .stdin('2')     # Valid quantity
        .stdin('')
        .stdout('\nThe order costs 17.81 €', regex=False)
        .exit(0))


@check50.check(compiles)
def case_insensitive():
    (check50.run('./snackbar')
        .stdin('burger')
        .stdin('2')         # Valid order for 2 Burgers
        .stdin('PIZZA')
        .stdin('1')         # Valid order for 1 Pizza
        .stdin('sALad')
        .stdin('3')         # Valid order for 3 Salads
        .stdin('')
        .stdout('\nThe order costs 41.54 €', regex=False)
        .exit(0))
