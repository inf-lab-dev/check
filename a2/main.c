#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(void)
{
    bmp_image* bmp = open_image("uni.bmp");

    if (bmp == NULL) {
        printf("Failed to load image\n");

        return 1;
    }

    printf("Image loaded: %dx%d\n", bmp->width, bmp->height);

    save_image(bmp, "output.bmp");
    close_image(bmp);

    return 0;
}