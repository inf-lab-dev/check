import check50
import check50.c

OUTPUT_HASH = ""

a2 = check50.import_checks('../a2')
from a2 import exists


@check50.check(exists)
def compiles():
    check50.c.compile('watermark.c')


@check50.check(compiles)
def overlays_image():
    check50.include('../uni.bmp')

    check50.c.valgrind('./watermark uni.bmp output.bmp').exit(0)

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
