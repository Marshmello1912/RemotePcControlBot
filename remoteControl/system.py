import os

from pyautogui import screenshot
from cv2 import VideoCapture, imwrite
from aiogram.types.input_file import BufferedInputFile, InputFile


def take_screenshot():
    screenshot('photo.png').tobytes()
    file = open('photo.png', 'rb')
    screen = BufferedInputFile(file, 'screenshot.png').from_file('photo.png', 'photo.png')
    file.close()
    os.remove("photo.png")
    return screen

def take_photo():
    cam = VideoCapture(0)
    result, image = cam.read()
    if result:
        imwrite('photo.png', image)
        file = open('photo.png', 'rb')
        photo = BufferedInputFile(file, 'photo.png').from_file('photo.png', 'photo.png')
        file.close()
        os.remove("photo.png")
        return photo
    else:
        return "Камера не найдена"


def turn_off_system():
    os.system("shutdown /s /f /t 0")


def reboot_system():
    os.system("shutdown /r /f /t 0")
