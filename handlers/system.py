from aiogram import types, Router, F
from aiogram.filters import StateFilter

from config import load_config
from remoteControl import system
from keyboards import keyboard
from states.state import Form

System_router = Router()

config = load_config()


async def take_screenshot(message: types.Message):
    result = system.take_screenshot()
    await message.answer_photo(result)


async def take_photo(message: types.Message):
    result = system.take_photo()
    if type(result) != str:
        await message.answer_photo(result)
    else:
        await message.answer(result)


async def turn_off(message: types.Message):
    await message.answer("Ваш компьютер будет выключен")
    system.turn_off_system()


async def reboot(message: types.Message):
    await message.answer("Ваш компьютер будет перезагружен")
    system.reboot_system()


System_router.message.register(take_screenshot, (F.text == keyboard.TakeScreenshot.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.System))
System_router.message.register(take_photo, (F.text == keyboard.TakePhoto.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.System))
System_router.message.register(turn_off, (F.text == keyboard.TurnOff.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.System))
System_router.message.register(reboot, (F.text == keyboard.Reboot.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.System))
