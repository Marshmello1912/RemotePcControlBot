import os


def turn_off_system():
    os.system("shutdown /s /f /t 0")


def reboot_system():
    os.system("shutdown /r /f /t 0")
