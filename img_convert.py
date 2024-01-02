import os
import sys
from PIL import Image


def check_args():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} folder_to_process")
        sys.exit(-1)


def get_img_files(folder):
    files = os.listdir(folder)
    return [f for f in files if f.endswith(".webp")]


def convert_imgs(filenames):
    for f in filenames:
        img = Image.open(f).convert("RGB")
        nf = f.replace(".webp", ".jpg")
        img.save(nf)
        print(".", end="")


if __name__ == "__main__":
    check_args()
    source_img_files = get_img_files(sys.argv[1])
    convert_imgs(source_img_files)