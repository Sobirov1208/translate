from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

til = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardButton("π¦πͺ Arabic",callback_data="ar"),
    InlineKeyboardButton("π·πΊ ΡΡΡΡΠΊΠΈΠΉ",callback_data="ru"),
    ],
    [
    InlineKeyboardButton("πΊπΏ Uzbekcha",callback_data="uz")
    ],
    [
    InlineKeyboardButton("π¬π§ English",callback_data="en"),
    InlineKeyboardButton("π°π· korean",callback_data="ko"),
    ]
  ]
)