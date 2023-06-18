# first aiogram project on Python with Git and GitHub

# Все Модули
from aiogram import Bot, Dispatcher, executor, types

# Основной код для работы с функциями бота
h_c = '''
Все доступные команды на данный момент:
/start - Запуск бота
/help - Вызов помощи
/support - Написать в поддержку
/description - Описание Dray
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



# Вход в систему использования ботом
_id = (985508783,) # Мой id в телеграм, то есть все пользователи кому доступен бот
admin_only = lambda message: message.from_user.id not in _id # Анонимная функция которая выдаёт bool значение при проверки является ли пользователь в acl
@dp.message_handler(admin_only, content_types=['any']) # проверяет если хотябы один из кортежа является True выдаёт доступ
async def handle_unwanted_users(message: types.Message): # функция которая удаляет нежелательных пользователей сообщения
    await bot.delete_message(message.chat.id, message.message_id)
    return




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
@dp.message_handler(commands=['secret']) # Вызов поддержки
async def support_(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEJZDpkjyiCq7JzLczhnaE7yRp7noNrawACQx0AAmt1-UkOzn3LS4oOBi8E')
    await message.delete()
@dp.message_handler() # автоматический ответ
async def auto_uns_(message: types.Message):
    await message.reply('Пожалуйста пользуйтесь командами!') # Написать сообщение которое отправил пользователь text=message.text



# Запуск Telegram бота
async def on_start(_):
    print('Бот успешно запущен!')
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start) # Запускаем бота