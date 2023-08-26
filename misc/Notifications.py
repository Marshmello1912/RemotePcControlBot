from aiogram import Dispatcher
from config import load_config
from keyboards import keyboard
from states.state import Form

config = load_config('.env')


async def start_notification(dp: Dispatcher):
    await dp.current_state(user=config.admin.adminId).set_state(state=Form.menu)
    await dp.bot.send_message(chat_id=config.admin.adminId,
                              text=f'{config.admin.adminName}, компьютер был запущен',
                              reply_markup=keyboard.rKeyboardMenu)


async def closing_notification(dp: Dispatcher):
    await dp.bot.send_message(chat_id=config.admin.adminId,
                              text=f'{config.admin.adminName}, компьютер был выключен '
                                   f'или перезагружен')
