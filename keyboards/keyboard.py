from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import load_config

config = load_config('.env')

BrowserStart = KeyboardButton(text='Запустить браузер')
OpenYoutube = KeyboardButton(text='Открыть ютуб')

StartSteam = KeyboardButton(text='Запустить Steam')
OpenGame = KeyboardButton(text=f'Запустить {config.steam.gameName}')

TakePhoto = KeyboardButton(text="Сделать фото с камеры")
TurnOff = KeyboardButton(text='Выключить ПК')
Reboot = KeyboardButton(text='Перезагрузить ПК')

Browser = KeyboardButton(text="Браузер")
Steam = KeyboardButton(text="Стим")
System = KeyboardButton(text='Система')

Exit = KeyboardButton(text="Назад")

rKeyboardBrowser = ReplyKeyboardMarkup(keyboard=[[BrowserStart, OpenYoutube], [Exit]], resize_keyboard=True)
rKeyboardSteam = ReplyKeyboardMarkup(keyboard=[[StartSteam, OpenGame], [Exit]], resize_keyboard=True)
rKeyboardSystem = ReplyKeyboardMarkup(keyboard=[[TurnOff, Reboot], [TakePhoto], [Exit]], resize_keyboard=True)

rKeyboardMenu = ReplyKeyboardMarkup(keyboard=[[Browser, Steam, System]], resize_keyboard=True)
