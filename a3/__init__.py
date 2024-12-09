import check50
import check50.c

a2 = check50.import_checks('../a2')
from a2 import *


@check50.check(exists)
def create():
    """The create function works correctly"""
    (check50.run('python3 todo.py')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdout('ToDo created successfully!')
        .stdin('1')
        .stdout('[0] Learn Inf-Einf')
        .stdin('0')
        .exit(0))


@check50.check(create)
def complete():
    """The complete function works correctly"""
    (check50.run('python3 todo.py')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('3')
        .stdin('0')
        .stdout('Successfully completed the ToDo!')
        .stdin('1')
        .stdout('[0] Learn Inf-Einf (completed)')
        .stdin('0')
        .exit(0))


@check50.check(create)
def complete_invalid():
    """The complete function rejects invalid indices"""
    (check50.run('python3 todo.py')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('3')
        .stdin('44')
        .stdout('ERROR: .*')
        .stdin('3')
        .stdin('-4')
        .stdout('ERROR: .*')
        .stdin('0')
        .exit(0))


@check50.check(create)
def delete():
    """The delete function works correctly"""
    (check50.run('python3 todo.py')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('4')
        .stdin('0')
        .stdout('Successfully deleted the ToDo!')
        .stdin('1')
        .stdout('No ToDos have been created yet.')
        .stdin('0')
        .exit(0))


@check50.check(create)
def delete_invalid():
    """The delete function rejects invalid indices"""
    (check50.run('python3 todo.py')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('4')
        .stdin('44')
        .stdout('ERROR: .*')
        .stdin('4')
        .stdin('-4')
        .stdout('ERROR: .*')
        .stdin('1')
        .stdout('[0] Learn Inf-Einf')
        .stdin('0')
        .exit(0))


@check50.check(create)
def update():
    """The update function works correctly"""
    (check50.run('python3 todo.py')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('5')
        .stdin('0')
        .stdin('Learn IntroSP')
        .stdout('Successfully updated the ToDo!')
        .stdin('1')
        .stdout('[0] Learn IntroSP')
        .stdin('0')
        .exit(0))


@check50.check(create)
def update_invalid():
    """The update function rejects invalid indices"""
    (check50.run('python3 todo.py')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('5')
        .stdin('44')
        .stdout('ERROR: .*')
        .stdin('5')
        .stdin('-4')
        .stdout('ERROR: .*')
        .stdin('0')
        .exit(0))
