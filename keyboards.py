from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

web_app = WebAppInfo(url="https://github.com/Elmurod31/Elmurod_burger.github.io")
web_app_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Web App", web_app=web_app)]
])