import check50
import check50.c

OUTPUT_HASH = 'a123f437a3f784a1f39f6cb7a384fb45347a1466d21d93bc02b5ba57c00a7a7c'


@check50.check()
def exists():
    check50.exists('watermark.c', 'overlay.bmp')
    check50.include('../a2/bmp.h')


@check50.check(exists)
def compiles():
    check50.c.compile('watermark.c')


@check50.check(compiles)
def overlays_image():
    check50.include('image.bmp')

    check50.c.valgrind('./watermark image.bmp output.bmp').exit(0)

    if check50.hash('output.bmp') != OUTPUT_HASH:
        raise check50.Failure(
            'The code does not overlay the image correctly.')


@check50.check(compiles)
def handles_dimension_error():
    check50.include('small.bmp')

    code = check50.c.valgrind('./watermark small.bmp output.bmp').exit()

    if code == 0:
        raise check50.Failure(
            'If the overlay image is too large for the input image, a non-zero exit code should be returned.')
