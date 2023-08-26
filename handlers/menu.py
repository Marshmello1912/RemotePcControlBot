from aiogram import Dispatcher, types
from states.state import Form
from keyboards import keyboard


async def exit_from_states(message: types.Message):
    await Form.menu.set()
    await message.answer('', reply_markup=keyboard.rKeyboardMenu)


async def steam(message: types.Message):
    await Form.Steam.set()
    await message.answer('', reply_markup=keyboard.rKeyboardSteam)


async def system(message: types.Message):
    await Form.System.set()
    await message.answer('', reply_markup=keyboard.rKeyboardSystem)


async def browser(message: types.Message):
    await Form.Browser.set()
    await message.answer('', reply_markup=keyboard.rKeyboardBrowser)


def register_menu_handlers(dp: Dispatcher):
    dp.register_message_handler(exit_from_states,lambda msg: msg.text == 'Назад' or msg.text == '/start', state="*")
    dp.register_message_handler(steam, lambda msg: msg.text == keyboard.Steam.text, state=Form.menu)
    dp.register_message_handler(browser, lambda msg: msg.text == keyboard.Browser.text, state=Form.menu)
    dp.register_message_handler(system, lambda msg: msg.text == keyboard.System, state=Form.menu)

