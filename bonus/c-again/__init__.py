import check50
import check50.c


@check50.check()
def exists():
    """todo.c exists"""
    check50.exists('todo.c')


@check50.check(exists)
def compiles():
    """todo.c compiles"""
    check50.c.compile('todo.c', lcs50=True)


@check50.check(compiles)
def create():
    """The create function works correctly"""
    (check50.c.valgrind('./todo')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdout('ToDo created successfully!')
        .stdin('1')
        .stdout('[0] Learn Inf-Einf', regex=False)
        .stdin('0')
        .exit(0))


@check50.check(create)
def complete():
    """The complete function works correctly"""
    (check50.c.valgrind('./todo')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('3')
        .stdin('0')
        .stdout('Successfully completed the ToDo!')
        .stdin('1')
        .stdout('[0] Learn Inf-Einf (completed)', regex=False)
        .stdin('0')
        .exit(0))


@check50.check(create)
def complete_invalid():
    """The complete function rejects invalid indices"""
    (check50.c.valgrind('./todo')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('3')
        .stdin('44')
        .stdout('INVALID: .*\n')
        .stdin('0')
        .exit(0))


@check50.check(create)
def delete():
    """The delete function works correctly"""
    (check50.c.valgrind('./todo')
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
    (check50.c.valgrind('./todo')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('4')
        .stdin('44')
        .stdout('INVALID: .*\n')
        .stdin('1')
        .stdout('[0] Learn Inf-Einf', regex=False)
        .stdin('0')
        .exit(0))


@check50.check(create)
def update():
    """The update function works correctly"""
    (check50.c.valgrind('./todo')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('5')
        .stdin('0')
        .stdin('Learn IntroSP')
        .stdout('Successfully updated the ToDo!')
        .stdin('1')
        .stdout('[0] Learn IntroSP', regex=False)
        .stdin('0')
        .exit(0))


@check50.check(compiles)
def update_invalid():
    """The update function rejects invalid indices"""
    (check50.c.valgrind('./todo')
        .stdin('2')
        .stdin('Learn Inf-Einf')
        .stdin('5')
        .stdin('44')
        .stdin('Learn IntroSP')
        .stdout('INVALID: .*\n')
        .stdin('0')
        .exit(0))
