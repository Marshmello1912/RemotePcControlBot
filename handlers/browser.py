from aiogram import types, Router, F
from aiogram.filters import StateFilter

from config import load_config
from remoteControl import browser
from keyboards import keyboard
from states.state import Form

Browser_router = Router()

config = load_config()


async def start_browser(message: types.Message):
    browser.start_browser()
    await message.answer("Браузер запущен")


async def open_youtube(message: types.Message):
    browser.open_youtube()
    await message.answer("Ютуб открыт")


Browser_router.message.register(start_browser, (F.text == keyboard.BrowserStart.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.Browser))
Browser_router.message.register(open_youtube, (F.text == keyboard.OpenYoutube.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.Browser))
