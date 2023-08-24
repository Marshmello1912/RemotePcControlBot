from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from config import load_config

config = load_config('.env')

browserStart = KeyboardButton('Запустить браузер')
OpenYoutube = KeyboardButton('Открыть ютуб')

StartSteam = KeyboardButton('Запустить Steam')
OpenGame = KeyboardButton(f'Запустить {config.steam.gameName}')

TurnOff = KeyboardButton('Выключить ПК')
Reboot = KeyboardButton('Перезагрузить ПК')

rKeyboard = ReplyKeyboardMarkup(resize_keyboard=True)
rKeyboard.row(browserStart, OpenYoutube)
rKeyboard.row(StartSteam, OpenGame)
rKeyboard.row(TurnOff, Reboot)
