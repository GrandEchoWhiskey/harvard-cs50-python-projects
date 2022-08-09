import os
import sys
from PIL import Image, ImageOps

err_no = [
    "Too few command-line arguments",
    "Too many command-line arguments",
    "Input does not exist",
    "Invalid output",
    "Input and output have different extensions"
]


def is_ext_valid(filename):
    _, ext = filename.split(".", maxsplit=1)
    return ext in ["jpg", "jpeg", "png"]


def is_ext_same(source, target):
    _, ext = source.split(".", maxsplit=1)
    return target.endswith(ext)


def dress_up(source, target):
    shirt = Image.open("shirt.png")
    photo = Image.open(source)
    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, shirt)
    photo.save(target)


def main():

    # Check input args
    if len(sys.argv) < 3: sys.exit(err_no[0])
    if len(sys.argv) > 3: sys.exit(err_no[1])
    if not os.path.isfile(sys.argv[1]): sys.exit(err_no[2])
    if not is_ext_valid(sys.argv[2]): sys.exit(err_no[3])
    if not is_ext_same(sys.argv[1], sys.argv[2]): sys.exit(err_no[4])

    # Dress Up
    dress_up(sys.argv[1], sys.argv[2])
    sys.exit(0)


if __name__ == "__main__":
    main()