from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

til = InlineKeyboardMarkup(
  inline_keyboard = [
    [
    InlineKeyboardButton("🇦🇪 Arabic",callback_data="ar"),
    InlineKeyboardButton("🇷🇺 русский",callback_data="ru"),
    ],
    [
    InlineKeyboardButton("🇺🇿 Uzbekcha",callback_data="uz")
    ],
    [
    InlineKeyboardButton("🇬🇧 English",callback_data="en"),
    InlineKeyboardButton("🇰🇷 korean",callback_data="ko"),
    ]
  ]
)