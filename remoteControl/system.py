import os
from cv2 import VideoCapture, imwrite


def take_photo():
    cam = VideoCapture(0)
    result, image = cam.read()
    if result:
        imwrite('photo.png', image)
        with open('photo.png', 'rb') as file:
            photo = file.read()
        os.remove("photo.png")
        return photo
    else:
        return "Камера не найдена"


def turn_off_system():
    os.system("shutdown /s /f /t 0")


def reboot_system():
    os.system("shutdown /r /f /t 0")
