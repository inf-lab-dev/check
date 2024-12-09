#
# THIS FILE HOLDS THE SAME CONTENT AS "a2/test_file.py"
#  (but needs to be duplicated for check50 to work properly)
#

from todo import ToDo, todos, show
import io


def test_init_task():
    assert ToDo('Learn Inf-Einf').task == 'Learn Inf-Einf'


def test_init_completed():
    assert not ToDo('Learn Inf-Einf').completed


def test_update():
    todo = ToDo('Learn Inf-Einf')
    todo.update('Learn IntroSP')

    assert todo.task == 'Learn IntroSP'
    assert not todo.completed


def test_complete():
    todo = ToDo('Learn Inf-Einf')

    assert not todo.completed

    todo.complete()

    assert todo.completed


def test_output(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1\n0'))

    todo1 = ToDo('Learn Inf-Einf')
    todo2 = ToDo('Learn IntroSP')

    todo2.complete()

    todos.append(todo1)
    todos.append(todo2)

    show()

    result = capsys.readouterr()

    assert '[0] Learn Inf-Einf\n' in result.out
    assert '[1] Learn IntroSP (completed)\n' in result.out
