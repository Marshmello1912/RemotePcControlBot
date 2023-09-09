import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.exceptions import TelegramNetworkError

import time

from config import load_config

from misc.Notifications import start_notification, closing_notification

from handlers.menu import register_menu_handlers
from handlers.steam import register_steam_handlers
from handlers.browser import register_browser_handlers
from handlers.system import register_system_handlers


logger = logging.getLogger(__name__)


def register_handlers(dp: Dispatcher):
    register_menu_handlers(dp)
    register_steam_handlers(dp)
    register_system_handlers(dp)
    register_browser_handlers(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %('
               u'message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.bot.botToken)
    dp = Dispatcher(storage=storage)
    register_handlers(dp)

    try:
        await start_notification(bot, dp)
        await dp.start_polling(bot)
    finally:
        await closing_notification(bot)
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    while True:
        try:
            asyncio.run(main())
        except (KeyboardInterrupt, SystemExit):
            logger.error("Bot stopped!")
            break
        except TelegramNetworkError:
            print(123)
            time.sleep(10)
