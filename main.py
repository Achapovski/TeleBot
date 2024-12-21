import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import get_config
from handlers.user_handlers import router, States
from keyboards.main_menu import load_main_menu
from middlewares.usrs import TrackUsersMiddleware, InputCodeWordMiddleware
from valid_models.models import Bot as BotModel


async def main():
    bot = Bot(token=get_config(model=BotModel, root_key="bot").token)

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router=router)
    dp.message.outer_middleware(InputCodeWordMiddleware())
    dp.message.middleware(TrackUsersMiddleware())
    await load_main_menu(bot=bot)
    await dp.start_polling(bot, start_date={})


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot was stopped")
