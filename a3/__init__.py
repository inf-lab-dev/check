from a2 import exists, compiles, prints_header, empty_input, single_item, multiple_items, invalid_item, case_insensitive
import check50
import check50.c

a2 = check50.import_checks('../a2')


@check50.check(compiles)
def out_of_stock():
    (check50.run('./snackbar')
        .stdin('Salad')  # Salad should have a quantity of 3
        .stdin('Salad')
        .stdin('Salad')
        .stdin('Salad')
        .stdout('Not enough dishes available.', regex=False)
        .stdin('')
        .stdout('\nThe order costs 17.81 €', regex=False)
        .exit(0))


@check50.check(compiles)
def mixed_items_with_stock():
    (check50.run('./snackbar')
        .stdin('Burger')  # Valid
        .stdin('Pasta')   # Invalid
        .stdout('The provided dish wasn\'t found', regex=False)
        .stdin('Soda')    # Valid
        .stdin('Salad')   # Valid (3 salads available)
        .stdin('Salad')   # Valid
        .stdin('Salad')   # Valid
        .stdin('Salad')   # Out of stock
        .stdout('Not enough dishes available.', regex=False)
        .stdin('')
        .stdout('\nThe order costs 24.88 €', regex=False)
        .exit(0))
