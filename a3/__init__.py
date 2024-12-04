import check50
import check50.c

a2 = check50.import_checks('../a2')
from a2 import *

@check50.check(a2.compiles)
def handles_missing_word_list():
    (check50.run('./search-zone random-file-that-does-not-exist.txt')
     .stdout('ERROR: Could not open random-file-that-does-not-exist.txt!', regex=False)
     .exit(1))
