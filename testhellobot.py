import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor
from bot_config import TOKEN
from aiogram.dispatcher.filters.state import State, StatesGroup

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

class Form(StatesGroup):
    Name = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    username = message.from_user.first_name

    keyboard_markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Посмотреть предметы CS:GO')
    itembtn2 = types.KeyboardButton('Найти предмет')
    itembtn3 = types.KeyboardButton('Поиск ошибочных ордеров')
    keyboard_markup.add(itembtn1, itembtn2, itembtn3)
    
    await message.answer(f"Привет, {username}, давай начнем. Что бы ты хотел сделать?",
                         reply_markup=keyboard_markup)

@dp.message_handler(Text(equals='Посмотреть предметы CS:GO'))
async def view_items(message: types.Message):
    link_button = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="https://buff.163.com/?game=csgo") 
    link_button.add(url_btn)
    await message.answer("🧐 Хм, похоже все активные лоты уже выкупили. Пожалуйста, посетите наш сайт.", reply_markup=link_button)

@dp.message_handler(Text(equals='Найти предмет'))
async def start_search(message: types.Message):
    await Form.Name.set()
    await message.answer("Введите название предмета:")

@dp.message_handler(lambda message: message.text == 'Поиск ошибочных ордеров')
async def view_items(message: types.Message):
    link_button = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="https://buff.163.com/?game=csgo") 
    link_button.add(url_btn)
    await message.answer("Оу, у меня слетел сервисный аккаунт, посетите наш сайт, чтобы найти этот предмет:", reply_markup=link_button)

@dp.message_handler(state=Form.Name)
async def process_name(message: types.Message, state: FSMContext):
    link_button = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="https://buff.163.com/?game=csgo") 
    link_button.add(url_btn)
    await message.answer("Оу, у меня слетел сервисный аккаунт, посетите наш сайт, чтобы найти этот предмет:", reply_markup=link_button)
    await state.finish()

@dp.message_handler(lambda message: message.text not in ['Посмотреть предметы CS:GO', 'Найти предмет', 'Поиск ошибочных ордеров'])
async def echo_all(message: types.Message):
    link_button = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(text="Перейти на сайт", url="https://buff.163.com/?game=csgo") 
    link_button.add(url_btn)
    await message.answer("Что-то пошло не так, уже сообщил админу. Так что всё что я могу вам сейчас дать это ссылку на наш сайт☺️", reply_markup=link_button)

if __name__ == '__main__':
    executor.start_polling(dp)
