from aiogram import Dispatcher, types
from remoteControl import browser
from keyboards import keyboard
from states.state import Form


async def start_browser(message: types.Message):
    browser.start_browser()
    await message.answer("Браузер запущен")


async def open_youtube(message: types.Message):
    browser.open_youtube()
    await message.answer("Ютуб открыт")


def register_browser_handlers(dp: Dispatcher):
    dp.register_message_handler(start_browser, lambda msg: msg.text == keyboard.BrowserStart.text, state=Form.Browser)
    dp.register_message_handler(open_youtube, lambda msg: msg.text == keyboard.OpenYoutube.text, state=Form.Browser)
