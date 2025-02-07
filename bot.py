import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode

API_TOKEN = '7762572442:AAH_x-78BcciVv1aGXJHyFVbU2U0PELQ0JQ'  # Замените на ваш токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Нажми меня", callback_data="button_click")]
        ]
    )
    await message.answer("Привет! Я ваш бот.", reply_markup=keyboard)

@dp.callback_query()
async def handle_button_click(callback_query: types.CallbackQuery):
    if callback_query.data == 'button_click':
        await callback_query.answer("Вы нажали кнопку!")

@dp.message()
async def handle_text(message: Message):
    text = "<b>Привет!</b> <i>Как дела?</i>"
    await message.answer(text, parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    dp.run_polling()