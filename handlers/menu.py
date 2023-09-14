from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext


from config import load_config
from states.state import Form
from keyboards import keyboard

Menu_router = Router()

config = load_config()


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


Menu_router.message.register(exit_from_states, ((F.text == 'Назад') | (F.text == '/start')) & (F.from_user.id == config.admin.adminId))
Menu_router.message.register(steam, (F.text == keyboard.Steam.text) & (F.from_user.id == config.admin.adminId))
Menu_router.message.register(browser, (F.text == keyboard.Browser.text) & (F.from_user.id == config.admin.adminId))
Menu_router.message.register(system, (F.text == keyboard.System.text) & (F.from_user.id == config.admin.adminId))

