# first aiogram project on Python with Git and GitHub

# Все Модули
from aiogram import Bot, Dispatcher, executor, types # Айограм асинхронная библеотека
from random import choice
'''
types - Помогает писать анотации в функциях
Dispatcher - Улавливает события в чате или события отправки сообщения боту
executor -  Для запуска бота в онлайн
choice - Из списка/кортежа задает рандомное значение
'''


# Основной код для работы с функциями бота
from variables import Hll_Bt, h_c, s_c, d_c



# Использование токена бота
f = open('API.txt', 'r')
TOKEN_API = f.readline() # Токен для подключения к telegram API
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
f.close()



# Вход в систему использования ботом
_id = (985508783,) # Мой id в телеграм, то есть все пользователи кому доступен бот
admin_only = lambda message: message.from_user.id not in _id # Анонимная функция которая выдаёт bool значение при проверки является ли пользователь в _id
@dp.message_handler(admin_only, content_types=['any']) # проверяет если хотябы один из кортежа является True выдаёт доступ
async def handle_unwanted_users(message: types.Message): # функция которая удаляет нежелательных пользователей сообщения
    await bot.delete_message(message.chat.id, message.message_id) # await ждёт пока в потоке появится свободное место
    return




# Ответов на сообщения и на команды
@dp.message_handler(commands=['description'])
async def desc_(message: types.Message): # В параметры функции попадает событие сообщения из чата
    await message.answer(d_c) # await ждёт пока в потоке появится свободное место
    await message.delete() # await ждёт пока в потоке появится свободное место
@dp.message_handler(commands=['start']) # Начало работы бота
async def start_(message: types.Message): # В параметры функции попадает событие сообщения из чата
    await message.answer(text=choice(Hll_Bt)) # await ждёт пока в потоке появится свободное место
    await message.delete() # await ждёт пока в потоке появится свободное место
@dp.message_handler(commands=['help']) # Вызов помощи
async def help_(message: types.Message): # В параметры функции попадает событие сообщения из чата
    await message.answer(text=h_c) # await ждёт пока в потоке появится свободное место
@dp.message_handler(commands=['support']) # Вызов поддержки
async def support_(message: types.Message):# В параметры функции попадает событие сообщения из чата
    await message.answer(text=s_c) # await ждёт пока в потоке появится свободное место
    await message.delete() # await ждёт пока в потоке появится свободное место
@dp.message_handler() # автоматический ответ
async def auto_uns_(message: types.Message): # В параметры функции попадает событие сообщения из чата
    if message.text.lower() in Hll_Bt: # Условие при котором отвечает на приветствие
        await message.answer('Людей не приветствую!')
    else:
        await message.reply('Пожалуйста пользуйтесь командами!') # await ждёт пока в потоке появится свободное место



# Запуск Telegram бота
async def on_start(_):
    print('Бот успешно запущен!')
executor.start_polling(dp, skip_updates=True, on_startup=on_start) # Скипаем абдейты при не онлайн