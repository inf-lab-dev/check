import check50
import check50.c

a1 = check50.import_checks('../a1')
from a1 import *

@check50.check(a1.compiles)
def handles_missing_word_list():
    (check50.run('./search-zone random-file-that-does-not-exist.txt')
     .stdout('ERROR: Could not open random-file-that-does-not-exist.txt!', regex=False)
     .exit(1))
