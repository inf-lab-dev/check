import check50
import check50.c


@check50.check()
def exists():
    check50.exists('search-zone.c')


@check50.check(exists)
def compiles():
    check50.c.compile('search-zone.c')


@check50.check(compiles)
def validates_arguments():
    (check50.run('./search-zone')
     .stdout('Usage: ./search-zone <words-file.txt>', regex=False)
     .exit(1))


@check50.check(compiles)
def quits_on_q():
    with open('words.txt', 'w') as f:
        f.write('q\n')

    (check50.run('./search-zone words.txt')
     .stdin('q')
     .exit(0))


@check50.check(compiles)
def single_word_in_list():
    with open('words.txt', 'w') as f:
        f.write('hello\n')

    run = check50.run('./search-zone words.txt')
    run.stdin('hello').stdout('\'hello\' is contained!', regex=False)
    run.stdin('world').stdout('\'world\' is NOT contained.', regex=False)
    run.stdin('q')


@check50.check(single_word_in_list)
def has_no_memory_leaks():
    with open('words.txt', 'w') as f:
        f.write('hello\n')

    (check50.c.valgrind('./search-zone words.txt')
     .stdin('hello')
     .stdin('q')
     .exit(0))


@check50.check(compiles)
def multiple_words_in_list():
    with open('psi.txt', 'w') as f:
        f.write('infeinf\n')
        f.write('introsp\n')
        f.write('eds\n')

    run = check50.run('./search-zone psi.txt')
    run.stdin('infeinf').stdout('\'infeinf\' is contained!', regex=False)
    run.stdin('introsp').stdout('\'introsp\' is contained!', regex=False)
    run.stdin('eiaps').stdout('\'eiaps\' is NOT contained.', regex=False)
    run.stdin('q')


@check50.check(multiple_words_in_list)
def case_insensitivity():
    run = check50.run('./search-zone psi.txt')
    run.stdin('InfEinf').stdout('\'InfEinf\' is contained!', regex=False)
    run.stdin('IntroSP').stdout('\'IntroSP\' is contained!', regex=False)
    run.stdin('q')
