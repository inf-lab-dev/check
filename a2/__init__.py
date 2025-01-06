import check50


@check50.check()
def exists():
    """todo.py exists"""
    check50.exists('todo.py')
    check50.include('test_file.py')


@check50.check(exists)
def todo_init_task():
    """ToDo's constructor initializes itself with given task"""
    check50.run('pytest test_file.py -k "test_init_task"').exit(0)


@check50.check(exists)
def todo_init_completed():
    """ToDo's constructor initializes completed to False"""
    check50.run('pytest test_file.py -k "test_init_completed"').exit(0)


@check50.check(exists)
def todo_update():
    """ToDo's update method replaces the task"""
    check50.run('pytest test_file.py -k "test_update"').exit(0)


@check50.check(exists)
def todo_complete():
    """ToDo's complete method completes the task"""
    check50.run('pytest test_file.py -k "test_complete"').exit(0)


@check50.check(exists)
def output_empty():
    """The output format of "show" is correct if no todos exist"""
    (check50.run('python3 todo.py')
        .stdin('1')
        .stdout('No ToDos have been created yet.')
        .stdin('0')
        .exit(0))


@check50.check(todo_complete)
def output_filled():
    """The output format of "show" is correct if todos exist"""
    check50.run('pytest test_file.py -k "test_output"').exit(0)
