import asyncio

from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

router = Router()


class States(StatesGroup):
    code_input_state = State()
    work_state = State()


@router.message(Command("prize"))
async def prize_process_message(message: Message, bot: Bot, **kwargs):
    await message.answer(text="💜")
    await asyncio.sleep(3)
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker="CAACAgQAAxkBAANwZ2ZijjQsHNCDB3ZkgtDTWxi78RsAAqARAAKm8XEeTuVB42urc0w2BA")


@router.message(Command("start"))
async def game_process_message(message: Message, bot: Bot, **kwargs):
    web_app = WebAppInfo(url=r"https://achapovski.github.io/WebSiteForBotApp/")

    button = InlineKeyboardButton(text="🎁", web_app=web_app)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(text="Открой меня!", reply_markup=keyboard)


@router.message(Command("clear"))
async def clear_state_process(message: Message, bot: Bot, state: FSMContext, **kwargs):
    message_id = message.message_id
    await state.set_data({})
    await asyncio.sleep(5)
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
