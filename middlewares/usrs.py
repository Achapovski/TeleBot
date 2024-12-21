import asyncio
from typing import Dict, Any, Awaitable, Callable, cast

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage, StorageKey, MemoryStorageRecord

from handlers.user_handlers import States

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Message


class TrackUsersMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ):
        message = cast(Message, event)
        if (message and message.from_user.first_name.lower() == "maxim"
                or message.from_user.username.lower() == "helenka_23" or message.from_user.username.lower() == "weessku"):
            return await handler(event, data)


class InputCodeWordMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ):
        message = cast(Message, event)
        code_word = "баншичка"

        bot: Bot | None = data.get("bot")
        state: FSMContext | None = data.get("state")

        if message.text.lower() == code_word:
            if not await state.get_value("code_word"):
                await bot.send_message(chat_id=message.from_user.id, text="Ааа, кажется, вы хотите кушац!")
            await state.update_data(code_word=code_word)

        if await state.get_value("code_word") == code_word and bot:
            return await handler(event, data)

        if bot:
            message_id = await bot.send_message(chat_id=message.from_user.id, text="Что вы делаете в моем холодильнике ???")

        await asyncio.sleep(2)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_id.message_id - 1)
        await asyncio.sleep(1)
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_id.message_id)

