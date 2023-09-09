from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext

from config import load_config
from keyboards import keyboard
from states.state import Form

config = load_config('.env')


async def start_notification(bot: Bot, dp: Dispatcher):
    await bot.send_message(chat_id=config.admin.adminId,
                           text=f'{config.admin.adminName}, компьютер был запущен',
                           reply_markup=keyboard.rKeyboardMenu)


async def closing_notification(bot: Bot):
    await bot.send_message(chat_id=config.admin.adminId,
                           text=f'{config.admin.adminName}, компьютер был выключен '
                                f'или перезагружен')
