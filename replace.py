from pygame import (display, image, transform,
                    init, quit)
from os import walk as listdir
from pathlib import Path


def is_image(filename: str):
    return filename.lower()[-3:] in ["bmp", "gif", "jpg", "lbm", "pbm", "pgm", "ppm", "pcx", "png", "pnm", "svg", "tga", "tif", "xpm"] or\
        filename.lower()[-4:] in ["jpeg", "tiff", "webp"] and filename != "icon.png"


def get_images():
    for path in listdir(gamedir):
        # If path is hidden
        if "." in path[0]:
            continue

        for file in path[2]:
            if is_image(file):
                yield Path(path[0]) / file


def routerize(filename: Path):
    image.save(transform.scale(ROUTER, image.load(filename).get_size()), filename, 'ROUTER')


if __name__ == "__main__":
    init()
    display.set_mode()

    gamedir = Path(__file__).parent
    ROUTER = image.load(gamedir/'icon.png')

    for i in get_images():
        routerize(i)

    quit()
