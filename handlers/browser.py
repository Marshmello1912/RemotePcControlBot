from aiogram import types, Router
from aiogram.filters import StateFilter

from remoteControl import browser
from keyboards import keyboard
from states.state import Form

Browser_router = Router()


async def start_browser(message: types.Message):
    browser.start_browser()
    await message.answer("Браузер запущен")


async def open_youtube(message: types.Message):
    browser.open_youtube()
    await message.answer("Ютуб открыт")


Browser_router.message.register(start_browser, lambda msg: msg.text == keyboard.BrowserStart.text, StateFilter(Form.Browser))
Browser_router.message.register(open_youtube, lambda msg: msg.text == keyboard.OpenYoutube.text, StateFilter(Form.Browser))
