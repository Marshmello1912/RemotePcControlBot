from aiogram import Dispatcher, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from states.state import Form
from keyboards import keyboard


async def exit_from_states(message: types.Message, state: FSMContext):
    await state.set_state(Form.menu)
    await message.answer('Вы вернулись в меню', reply_markup=keyboard.rKeyboardMenu)


async def steam(message: types.Message, state: FSMContext):
    await state.set_state(Form.Steam)
    await message.answer('Открыть стим или запустить игру?', reply_markup=keyboard.rKeyboardSteam)


async def system(message: types.Message, state: FSMContext):
    await state.set_state(Form.System)
    await message.answer('Выключить или перезагрузить пк?', reply_markup=keyboard.rKeyboardSystem)


async def browser(message: types.Message, state: FSMContext):
    await state.set_state(Form.Browser)
    await message.answer('Открыть браузер?', reply_markup=keyboard.rKeyboardBrowser)


def register_menu_handlers(dp: Dispatcher):
    dp.message.register(exit_from_states, lambda msg: msg.text == 'Назад' or msg.text == '/start')
    dp.message.register(steam, lambda msg: msg.text == keyboard.Steam.text)
    dp.message.register(browser, lambda msg: msg.text == keyboard.Browser.text)
    dp.message.register(system, lambda msg: msg.text == keyboard.System.text)

