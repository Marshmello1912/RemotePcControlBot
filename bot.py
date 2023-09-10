import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.exceptions import TelegramNetworkError

import time

from config import load_config

from misc.Notifications import start_notification, closing_notification

from handlers.menu import Menu_router
from handlers.steam import Steam_router
from handlers.browser import Browser_router
from handlers.system import System_router

logger = logging.getLogger(__name__)


def register_handlers(dp: Dispatcher):
    dp.include_router(Menu_router)
    dp.include_router(Steam_router)
    dp.include_router(System_router)
    dp.include_router(Browser_router)


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
            time.sleep(10)
