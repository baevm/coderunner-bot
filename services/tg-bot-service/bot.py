import asyncio
import logging
import sys
from textwrap import dedent
from aiogram import types
from magic_filter import F

from config import config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hpre
from aiogram.enums import ParseMode

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    kb = [
        [types.KeyboardButton(text="/run")],
        [types.KeyboardButton(text="/benchmark")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, 
                                         resize_keyboard=True, 
                                         one_time_keyboard=True)
    
    await message.answer(f"Привет, {hbold(message.from_user.full_name)}!", reply_markup=keyboard)

@dp.message(Command("run"))
async def run_handler(message:Message):
    msg_txt = dedent('''\
            Введите код в формате:
            ```python
            print("hello world!")
            ```
            ''')
    await message.answer(msg_txt)

@dp.message(Command("benchmark"))
async def run_handler(message:Message):
    await message.answer("todo")

@dp.message(F.md_text.contains("```"))
async def get_code_handler(message: Message):
    print(message.md_text)
    await message.reply("Got your code")


async def main():
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())