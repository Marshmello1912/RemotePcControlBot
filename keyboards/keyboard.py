from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from config import load_config

config = load_config('.env')

BrowserStart = KeyboardButton('Запустить браузер')
OpenYoutube = KeyboardButton('Открыть ютуб')

StartSteam = KeyboardButton('Запустить Steam')
OpenGame = KeyboardButton(f'Запустить {config.steam.gameName}')

TurnOff = KeyboardButton('Выключить ПК')
Reboot = KeyboardButton('Перезагрузить ПК')

Browser = KeyboardButton("Браузер")
Steam = KeyboardButton("Стим")
System = KeyboardButton('Система')

Exit = KeyboardButton("Назад")

rKeyboardBrowser = ReplyKeyboardMarkup(resize_keyboard=True).row(BrowserStart, OpenYoutube).add(Exit)
rKeyboardSteam = ReplyKeyboardMarkup(resize_keyboard=True).row(StartSteam, OpenGame).add(Exit)
rKeyboardSystem = ReplyKeyboardMarkup(resize_keyboard=True).row(TurnOff, Reboot).add(Exit)

rKeyboardMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(Browser, Steam, System)
