from aiogram import types, Router, F
from aiogram.filters import StateFilter

from config import load_config
from remoteControl import steam
from keyboards import keyboard
from states.state import Form

Steam_router = Router()

config = load_config()


async def start_steam(message: types.Message):
    resp = steam.start_steam()
    await message.answer(resp)


async def start_game(message: types.Message):
    resp = steam.start_game()
    await message.answer(resp)


Steam_router.message.register(start_steam, (F.text == keyboard.StartSteam.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.Steam))
Steam_router.message.register(start_game, (F.text == keyboard.OpenGame.text) & (F.from_user.id == config.admin.adminId), StateFilter(Form.Steam))
