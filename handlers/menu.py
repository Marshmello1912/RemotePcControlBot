from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from states.state import Form
from keyboards import keyboard

Menu_router = Router()


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


Menu_router.message.register(exit_from_states, lambda msg: msg.text == 'Назад' or msg.text == '/start')
Menu_router.message.register(steam, lambda msg: msg.text == keyboard.Steam.text)
Menu_router.message.register(browser, lambda msg: msg.text == keyboard.Browser.text)
Menu_router.message.register(system, lambda msg: msg.text == keyboard.System.text)

