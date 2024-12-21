from aiogram import Bot
from aiogram.types import BotCommand


async def load_main_menu(bot: Bot):
    main_commands = [
        BotCommand(command="start", description="Запускает бота и..."),
        BotCommand(command="prize", description="???"),
    ]
    await bot.set_my_commands(main_commands)
