from aiogram import Dispatcher, types
from remoteControl import steam


async def start_steam(message: types.Message):
    resp = steam.start_steam()
    await message.answer(resp)


async def start_game(message: types.Message):
    resp = steam.start_game()
    await message.answer(resp)


def register_steam_handlers(dp: Dispatcher):
    dp.register_message_handler(start_steam, lambda msg: msg.text == "Запустить Steam")
    dp.register_message_handler(start_game, lambda msg: msg.text == f"Запустить {steam.config.steam.gameName}")

