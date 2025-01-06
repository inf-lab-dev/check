import check50

a3 = check50.import_checks('../a3')
from a3 import *


@check50.check(exists)
def tests_exist():
    """test_todo.py exists"""
    check50.exists('test_todo.py')


@check50.check(tests_exist)
def student_file_passes():
    """Implementation of ToDo passes all tests in test_todo.py"""
    check50.run('pytest test_todo.py').exit(0)
