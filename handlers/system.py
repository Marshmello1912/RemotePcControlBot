from aiogram import types, Router
from aiogram.filters import StateFilter

from remoteControl import system
from keyboards import keyboard
from states.state import Form

System_router = Router()


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


System_router.message.register(take_photo, lambda msg:msg.text == keyboard.TakePhoto.text, StateFilter(Form.System))
System_router.message.register(turn_off, lambda msg: msg.text == keyboard.TurnOff.text, StateFilter(Form.System))
System_router.message.register(reboot, lambda msg: msg.text == keyboard.Reboot.text, StateFilter(Form.System))
