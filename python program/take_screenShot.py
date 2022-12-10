# Date: 06-01-2021
# python_program to take screenshot

from PIL import ImageGrab  # pip install pillow


def takeScreenShot():
    image = ImageGrab.grab()
    image.show()


if __name__ == '__main__':
    takeScreenShot()
