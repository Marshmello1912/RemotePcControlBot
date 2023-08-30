from aiogram import Dispatcher, types
from remoteControl import system
from keyboards import keyboard
from states.state import Form


async def take_photo(message: types.Message):
    result = system.take_photo()
    if type(result) == bytes:
        await message.answer_photo(result)
    else:
        await message.answer(result)


async def turn_off(message: types.Message):
    await message.answer("Ваш компьютер будет выключен")
    system.turn_off_system()


async def reboot(message: types.Message):
    await message.answer("Ваш компьютер будет перезагружен")
    system.reboot_system()


def register_system_handlers(dp: Dispatcher):
    dp.register_message_handler(take_photo, lambda msg:msg.text == keyboard.TakePhoto.text, state=Form.System)
    dp.register_message_handler(turn_off, lambda msg: msg.text == keyboard.TurnOff.text, state=Form.System)
    dp.register_message_handler(reboot, lambda msg: msg.text == keyboard.Reboot.text, state=Form.System)
