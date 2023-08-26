from aiogram import Dispatcher, types
from pyarmor.helper.build_data_module import key

from remoteControl import steam
from keyboards import keyboard

async def start_steam(message: types.Message):
    resp = steam.start_steam()
    await message.answer(resp)


async def start_game(message: types.Message):
    resp = steam.start_game()
    await message.answer(resp)


def register_steam_handlers(dp: Dispatcher):
    dp.register_message_handler(start_steam, lambda msg: msg.text == keyboard.StartSteam.text)
    dp.register_message_handler(start_game, lambda msg: msg.text == keyboard.OpenGame.text)

