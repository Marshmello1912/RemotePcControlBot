import os
from config import load_config

config = load_config('.env')


def start_steam():
    try:
        os.startfile(config.steam.steamPath)
    except FileNotFoundError:
        return "Путь к стим указан не правильно"
    else:
        return "Стим успешно запущен"


def start_game():
    try:
        os.startfile(config.steam.gamePath)
    except FileNotFoundError:
        return f"Путь к {config.steam.gameName} указан не верно"
    else:
        return f"{config.steam.gameName} работает"
