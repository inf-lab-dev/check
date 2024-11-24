import check50
import check50.c

MAIN_FUNCTION = """
int main(void)
{
    bmp_image* bmp = open_image("image.bmp");

    if (bmp == NULL) {
        printf("Failed to load image\\n");

        return 1;
    }

    printf("Image loaded: %dx%d\\n", bmp->width, bmp->height);

    save_image(bmp, "output.bmp");
    close_image(bmp);

    return 0;
}
"""


@check50.check()
def exists():
    check50.exists('watermark.c')
    check50.include('bmp.h', 'image.bmp')


@check50.check(exists)
def has_no_main_function():
    with open('watermark.c') as f:
        code = f.read()

    if 'int main' in code:
        raise check50.Failure(
            'You should not implement a "main" function in the second task!')


@check50.check(has_no_main_function)
def functions_correctly_implemented():

    with open('watermark.c', 'a') as f:
        f.write(MAIN_FUNCTION)

    check50.c.compile('watermark.c')
    (check50.c.valgrind('./watermark')
     .stdout('Image loaded: 1425x600', regex=False)
     .exit(0))

    if check50.hash('output.bmp') != check50.hash('image.bmp'):
        raise check50.Failure(
            'The code does not produce the same file when saving an unmodified image.')
