# first aiogram project on Python with Git and GitHub

# Все Модули
from aiogram import Bot, Dispatcher, executor, types

# Основной код для работы с функциями бота
h_c = '''
Все доступные команды на данный момент:
/start - Запуск бота
/help - Вызов помощи
/support - Написать в поддержку
''' # Вывод функции помощи
s_c = '''
Чтобы обратиться в службу поддержки напишите письмо!
На электронную почту указанную ниже:
solomko2020@yandex.ru
''' # Вывод функции поддержки
d_c = '''
Это Telegram бот, был создан чтобы удалить (
Если конечно в него не задонатят 99999999999999999$
Спасите котю!
''' # Описание бота




# Использование токена бота
f = open('API.txt', 'r')
TOKEN_API = f.readline() # Токен для подключения к telegram API
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
f.close()



# Ответов на сообщения и на команды
@dp.message_handler(commands=['description'])
async def desc_(message: types.Message):
    await message.answer(d_c)
    await message.delete()
@dp.message_handler(commands=['start']) # Начало работы бота
async def start_(message: types.Message):
    await message.answer(text='Памагите, мой хозяин хочет меня удалить :( !')
    await message.delete()
@dp.message_handler(commands=['help']) # Вызов помощи
async def help_(message: types.Message):
    await message.answer(text=h_c)
@dp.message_handler(commands=['support']) # Вызов поддержки
async def support_(message: types.Message):
    await message.answer(text=s_c)
    await message.delete()
@dp.message_handler() # автоматический ответ
async def auto_uns_(message: types.Message):
    await message.reply('Пожалуйста пользуйтесь командами!') # Написать сообщение которое отправил пользователь text=message.text



# Запуск Telegram бота
if __name__ == '__main__':
    executor.start_polling(dp) # Запускаем бота