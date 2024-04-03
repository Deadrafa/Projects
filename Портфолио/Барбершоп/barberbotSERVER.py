import asyncio
import logging
import mysql.connector
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
from aiogram import F
import sicret 
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from timeforem import formatted_date_day, proverka, formatted_date_moth
from keyboard import get_reply_keyboard_onOnehour, get_reply_keyboard_half_and_hour, get_reply_keyboard_half_hour, get_reply_keyboard_finish, get_reply_keyboard_finish1, get_reply_keyboard_finish2, get_reply_keyboard_MYSQL
from keyboard import get_keyboard
from data import mydate

listmain = []
user_list = []

boty = Bot(token=sicret.TOKEN)
dp = Dispatcher()

 #Если нужно принять список input_list = []
price = FSInputFile('photo_2023-12-23_20-06-39.jpg')


priselist = [
           [types.KeyboardButton(text="Мужская стрижка\n(Ножницы + машинка)")],
           [types.KeyboardButton(text="Фэйд\n(Плавный переход с ноля)")],
           [types.KeyboardButton(text="Стрижка машинкой\n(Одна две насадки)")],
           [types.KeyboardButton(text="Детская стрижка\n(До 14 лет)")],
           [types.KeyboardButton(text="Стрижка бороды")],
           [types.KeyboardButton(text="Камуфляж головы")],
           [types.KeyboardButton(text="Камуфляж бороды")],
           [types.KeyboardButton(text="КОМПЛЕКС - голова+борода")]
    ]
PRlist = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=priselist)

@dp.message(CommandStart())
async def process_start_command(message: types.Message):
    kb = [
           [types.KeyboardButton(text="📅Записаться на стрижку📅")],
           [types.KeyboardButton(text="💰Посмотреть price лист💰")],
           [types.KeyboardButton(text="👨🏻‍💻Служба поддержки👨🏻‍💻")]
    ]
    Keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    await message.answer(f"Здравствуйте, {message.from_user.first_name}👋!")
    await message.answer(f"{message.from_user.first_name}\nВыберите действие:", reply_markup=Keyboard)

@dp.message(Command('id'))
async def id(message: types.Message):
    await message.reply(f'Ваш id: {message.from_user.id}')
    await message.answer("Нажмите чтобы зарегестрироваться", reply_markup=get_reply_keyboard_MYSQL())
    await boty.send_sticker(chat_id=message.from_user.id, sticker="CAACAgIAAxkBAAELM0Rlp6iGUcWpxewrrr4AAdxTDijtSkYAAiMAAygPahQnUSXnjCCkBjQE")

@dp.message(Command('чат'))
async def get_chat_id(message: types.Message):
    chat_id = message.chat.id
    await message.reply(f"ID вашего чата: {chat_id}")


@dp.message(F.text == "💰Посмотреть price лист💰")
async def photo(message: types.Message):
       await boty.send_photo(chat_id=message.from_user.id, photo=price)

@dp.message(F.text =="📅Записаться на стрижку📅")
async def yslyga(message: types.Message):
    await message.answer(
        "Выберите услугу",
        reply_markup=get_keyboard()
    )

@dp.callback_query(F.data == "strilka_def")
async def call_yslyga1(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth ) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("Мужская стрижка")
    user_list.clear()
    user_list.append("Мужская стрижка")
    print(listmain)
    print(user_list)
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.callback_query(F.data == "feid")
async def call_feid(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth ) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("Фэйд")
    user_list.clear()
    user_list.append("Фэйд")
    print(listmain)
    print(user_list) 
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.callback_query(F.data == "ctrijkaMashinkoi")
async def call_yslyga2(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth ) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("Стрижка машинкой")
    user_list.clear()
    user_list.append("Стрижка машинкой")
    print(listmain)
    print(user_list) 
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.callback_query(F.data == "kids_strichka")
async def call_yslyga4(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth ) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("Детская стрижка\n(До 14 лет)")
    user_list.clear()
    user_list.append("Детская стрижка")
    print(listmain)
    print(user_list) 
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.callback_query(F.data == "boroda_strich")
async def call_yslyga5(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth ) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("Стрижка бороды")
    user_list.clear()
    user_list.append("Стрижка бороды")
    print(listmain)
    print(user_list) 
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.callback_query(F.data == "golova_kamyflij")
async def call_yslyga6(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth ) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("Камуфляж головы")
    user_list.clear()
    user_list.append("Камуфляж головы")
    print(listmain)
    print(user_list) 
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.callback_query(F.data == "boroda_kamyflij")
async def call_yslyga7(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth ) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("Камуфляж бороды")
    user_list.clear()
    user_list.append("Камуфляж бороды")
    print(listmain)
    print(user_list) 
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.callback_query(F.data == "Kompleksiks")
async def call_yslyga8(callback: types.CallbackQuery):
    listmain.clear()
    builder = ReplyKeyboardBuilder()
    for i in range(int(formatted_date_day), (proverka(formatted_date_moth) + 1)):
        builder.add(types.KeyboardButton(text=str(i)))
        poteranaia_I = i
        listmain.append(poteranaia_I)
    listmain.append("КОМПЛЕКС - голова+борода")
    user_list.clear()
    user_list.append("КОМПЛЕКС - голова+борода")
    print(listmain)
    print(user_list) 
    builder.adjust(7)
    await callback.message.answer(
        f'Выберите дату на {mydate.strftime("%B")}:',
          reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.message(lambda message: any(str(day) in message.text for day in listmain))
async def time(message: types.Message):
    user_list.append(message.text)
    print(user_list)
    if("Мужская стрижка" == listmain[-1] or "Фэйд" == listmain[-1] or "Детская стрижка\n(До 14 лет)" == listmain[-1] in listmain):
       await message.answer('Выберите время с промежутком в час:', reply_markup=get_reply_keyboard_onOnehour())
       listmain.clear()
    if("КОМПЛЕКС - голова+борода" == listmain[-1] in listmain):
       await message.answer('Выберите с промежутком в полтора часа:', reply_markup=get_reply_keyboard_half_and_hour())
       listmain.clear()
    if("Стрижка машинкой" == listmain[-1] or "Стрижка бороды" == listmain[-1] or "Камуфляж головы" == listmain[-1] or "Камуфляж бороды" == listmain[-1] in listmain):
       await message.answer('Выберите с промежутком в пол часа', reply_markup=get_reply_keyboard_half_hour())
       listmain.clear()


@dp.callback_query(F.data == "Registr_users")
async def call_finish(callback: types.CallbackQuery):
    db = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='client'
    )
    cursor = db.cursor()
    cursor.execute("SELECT name, user_id FROM people")
    result = cursor.fetchall()
    people_list = [f'{callback.from_user.first_name}', int(f'{callback.from_user.id}')]
    print(people_list)
    for row in result:
        row = list(row)
        print(row)
        if(row == people_list):
            await callback.message.answer("😡Вы уже зарегестрированы😡")
            break
    if(row != people_list):
        sql = "INSERT INTO people (name, user_id) VALUES (%s, %s)"
        val = (f'{callback.from_user.first_name}', f'{callback.from_user.id}')
        mylist = list(val)
        cursor.execute(sql, mylist)
        db.commit()
        print(cursor.rowcount, "запись добавлена")
        await callback.message.answer("✅Я вас зарегестрировал✅")

@dp.callback_query(F.data == "10:00 - 11:00")
async def call_finish(callback: types.CallbackQuery):
    await callback.message.answer("✅Нажмите на кнопку записаться✅", reply_markup=get_reply_keyboard_finish())

@dp.callback_query(F.data == "11:00 - 12:00")
async def call_finish(callback: types.CallbackQuery):
    await callback.message.answer("✅Нажмите на кнопку записаться✅", reply_markup=get_reply_keyboard_finish1())

@dp.callback_query(F.data == "12:00 - 13:00")
async def call_finish(callback: types.CallbackQuery):
    await callback.message.answer("✅Нажмите на кнопку записаться✅", reply_markup=get_reply_keyboard_finish2())
    
@dp.callback_query(F.data == "finish_reg")
async def finish(callback: types.CallbackQuery):
    await boty.send_message(chat_id=sicret.admin_id, text= f'Запись:\nИмя: {callback.from_user.first_name}\nУслуга: {user_list[0]}\nДата записи: {user_list[-1]} {mydate.strftime("%B")}\nВремя: (10:00 - 11:00)')
    await callback.message.answer("Вы успешно записаны😇\nСпасибо что воспользовались ботом")
    user_list.clear() #Не забудь почистить user_list с помошью user_list.clear()

@dp.callback_query(F.data == "finish_reg1")
async def finish(callback: types.CallbackQuery):
    await boty.send_message(chat_id=sicret.admin_id, text= f'Запись:\nИмя: {callback.from_user.first_name}\nУслуга: {user_list[0]}\nДата записи: {user_list[-1]} {mydate.strftime("%B")}\nВремя: (11:00 - 12:00)')
    await callback.message.answer("Вы успешно записаны😇\nСпасибо что воспользовались ботом")
    user_list.clear() #Не забудь почистить user_list с помошью user_list.clear()

@dp.callback_query(F.data == "finish_reg2")
async def finish(callback: types.CallbackQuery):
    await boty.send_message(chat_id=sicret.admin_id, text= f'Запись:\nИмя: {callback.from_user.first_name}\nУслуга: {user_list[0]}\nДата записи: {user_list[-1]} {mydate.strftime("%B")}\nВремя: (12:00 - 13:00)')
    await callback.message.answer("Вы успешно записаны😇\nСпасибо что воспользовались ботом")
    user_list.clear() #Не забудь почистить user_list с помошью user_list.clear()


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    logging.basicConfig(level=logging.INFO)
    # And the run events dispatching
    await dp.start_polling(boty, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
	print("start")
	asyncio.run(main())