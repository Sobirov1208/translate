from googletrans import Translator
import logging
from aiogram import Bot, Dispatcher, executor, types
from button import *
from aiogram.types import Message , CallbackQuery

API_TOKEN = '5013302766:AAHtp5Flsn6dmcjBbAJCtEKDK7ZCMIrNNfM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  javob = f"*Assalomu Alaykum* *{message.from_user.first_name}*"
  javob += "\n\n*Tarjima qilmoqchi bo'lgan So'zni yoki matnni kiriting : *"
  await message.reply(javob,parse_mode="markdown")

@dp.message_handler()
async def text(message: types.Message):
  global msg
  msg = message.text

  await message.answer("*Tilni tanlang!*",reply_markup= til ,parse_mode="markdown")
@dp.callback_query_handler(text="ru")
async def til_tanlash(call: CallbackQuery):
  res = translator.translate(msg, dest="ru")
  await call.message.answer(res.text)

@dp.callback_query_handler(text="ar")
async def til_tanlash(call: CallbackQuery):
  res = translator.translate(msg, dest="ar")
  await call.message.answer(res.text)

@dp.callback_query_handler(text="uz")
async def til_tanlash(call: CallbackQuery):
  res = translator.translate(msg, dest="uz")
  await call.message.answer(res.text)

@dp.callback_query_handler(text="en")
async def til_tanlash(call: CallbackQuery):
  res = translator.translate(msg, dest="en")
  await call.message.answer(res.text)
  
@dp.callback_query_handler(text="ko")
async def til_tanlash(call: CallbackQuery):
  res = translator.translate(msg, dest="ko")
  await call.message.answer(res.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)