# first aiogram project on Python with Git and GitHub
from aiogram import Bot, Dispatcher, executor, types
#import requests

# https://api.telegram.org/bot<token>/METHOD_NAME
TOKEN_API = '6036510465:AAFBx2_YguG4K7XtDsW23lvlRRDx7OIBkag' # Токен для подключения к telegram API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp) # Запускаем бота