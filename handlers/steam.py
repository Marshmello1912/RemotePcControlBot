from aiogram import types, Router
from aiogram.filters import StateFilter

from remoteControl import steam
from keyboards import keyboard
from states.state import Form

Steam_router = Router()


async def start_steam(message: types.Message):
    resp = steam.start_steam()
    await message.answer(resp)


async def start_game(message: types.Message):
    resp = steam.start_game()
    await message.answer(resp)


Steam_router.message.register(start_steam, lambda msg: msg.text == keyboard.StartSteam.text, StateFilter(Form.Steam))
Steam_router.message.register(start_game, lambda msg: msg.text == keyboard.OpenGame.text, StateFilter(Form.Steam))
