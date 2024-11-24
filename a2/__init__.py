import check50
import check50.c


@check50.check()
def exists():
    check50.exists('watermark.c')
    check50.include('bmp.h', 'uni.bmp')


@check50.check(exists)
def has_no_main_function():
    with open('watermark.c') as f:
        code = f.read()

    if 'int main' in code:
        raise check50.Failure(
            'You should not implement a "main" function in the second task!')


@check50.check(has_no_main_function)
def functions_correctly_implemented():
    check50.include('main.c')

    check50.c.compile('watermark.c', 'main.c')
    (check50.c.valgrind('./main')
     .stdout('Image loaded: 3x3', regex=False)
     .exit(0))

    if check50.hash('output.bmp') != check50.hash('uni.bmp'):
        raise check50.Failure(
            'The code does not produce the same file when saving an unmodified image.')
