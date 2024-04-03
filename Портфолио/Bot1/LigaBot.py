import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.types import FSInputFile
import sicret 
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keyboarLig import get_keyboard, get_keyboard2, get_poisk, get_keyboard3, get_poisk2, get_Point, get_Rep, get_poisk3, get_sort
import csv
import pandas as pd
from open2 import poisk, poisk2
import psycopg2
import subprocess


TOKEN = ""
admin_id = '' 

boty = Bot(token=sicret.TOKEN)
dp = Dispatcher()
# avatar = FSInputFile('avatar.jpg')
User_List = {'Dead': FSInputFile('avatar.jpg'),
			 'avatar2': FSInputFile('avatar.jpg')}
Main_list = []
Main_list.clear()


kb = [
           [types.KeyboardButton(text="📊Посмотреть рейтинг📊")],
           [types.KeyboardButton(text="💰Посмотреть price лист💰")],
           [types.KeyboardButton(text="👨🏻‍💻Служба поддержки👨🏻‍💻")]
		   ]
Keyboard = types.ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)

kb_us = [
           [types.KeyboardButton(text="📊Посмотреть рейтинг📊")]
		   ]
Keyboard_US = types.ReplyKeyboardMarkup(keyboard=kb_us,resize_keyboard=True)



if sicret.admin_id != 951789343:
	@dp.message(CommandStart())
	async def process_start_command(message: types.Message):
		await message.answer(f'"Здравствуйте, {message.from_user.first_name}👋!\nВы обычный пользователь')
		await message.answer(f"{message.from_user.first_name}\nВыберите действие:", reply_markup=Keyboard_US)
		
				
else:
	@dp.message(Command('top'))
	async def get_chat_id(message: types.Message):
		await boty.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
		await message.answer(f"Начало Нового Списка")
		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		cur.execute("SELECT * FROM ligatable ORDER BY ligaPoints DESC")

	# получаем результат
		rows = cur.fetchall()
		i = 1
		for row in rows:
			if(row[3] in ['Dead']):
				await boty.send_photo(chat_id=message.from_user.id,photo=User_List['Dead'],caption=f"Место: {i}\nИмя: {row[1]}\nФамилия: {row[2]}\nНик: {row[3]}\nLigaPoint: {row[4]}\nRep: {row[5]}")
				i += 1
			else:
				await message.answer(f"Место: {i}\nИмя: {row[1]}\nФамилия: {row[2]}\nНик: {row[3]}\nLigaPoint: {row[4]}\nRep: {row[5]}")
				i += 1
		# print(row)

	# закрываем соединение
		conn.close()


	@dp.message(CommandStart())	
	async def process_start_command(message: types.Message):
		await message.answer(f"Hi, admin -_-")
		await message.answer(f"{message.from_user.first_name}\nВыберите действие:", reply_markup=get_keyboard())
	@dp.callback_query(F.data == "add_user")
	async def call_finish(callback: types.CallbackQuery):
		await callback.message.answer("Введите Имя, Фамилию и никнейм:\nПример: Иван Иванов nickname", reply_markup=get_keyboard2())
	@dp.callback_query(F.data == "name")
	async def call_finish(callback: types.CallbackQuery):
		await callback.message.answer(f'Введите Имя')
		
	# @dp.callback_query(F.data == "sort")
	# async def call_finish(callback: types.CallbackQuery):
	# 	await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
	# 	await callback.message.answer(f'сортировка')

	@dp.callback_query(F.data == "second_name")
	async def call_finish(callback: types.CallbackQuery):
		await callback.message.answer(f'Введите Фамилию')


	@dp.callback_query(F.data == "nickname")
	async def call_finish(callback: types.CallbackQuery):
		await callback.message.answer(f'Введите никнейм')
		
	@dp.callback_query(F.data == "LigaPoints")
	async def call_finish(callback: types.CallbackQuery):
		await callback.message.answer(f'Введите никнейм, кому начислить?', reply_markup=get_poisk2())


	@dp.callback_query(F.data == "Reiting")
	async def call_finish(callback: types.CallbackQuery):
		await callback.message.answer(f'Введите никнейм, кому начислить?', reply_markup=get_poisk3())



	@dp.callback_query(F.data == "nalik")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Сколько начисличь?', reply_markup=get_Point())

	@dp.callback_query(F.data == "anal")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Сколько начисличь?', reply_markup=get_Rep())


	@dp.callback_query(F.data == "five")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 5 LigaPoint')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print(row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  ligaPoints = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			ligaPoints = str(int(nick + 5))

			# Выполните SQL-запрос
			cur.execute(update_sql, (ligaPoints, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")

	@dp.callback_query(F.data == "four")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 4 LigaPoint')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print(row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  ligaPoints = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			ligaPoints = str(int(nick + 4))

			# Выполните SQL-запрос
			cur.execute(update_sql, (ligaPoints, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")


	@dp.callback_query(F.data == "free")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 3 LigaPoint')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print(row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  ligaPoints = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			ligaPoints = str(int(nick + 3))

			# Выполните SQL-запрос
			cur.execute(update_sql, (ligaPoints, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")



	@dp.callback_query(F.data == "two")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 2 LigaPoint')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print(row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  ligaPoints = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			ligaPoints = str(int(nick + 2))

			# Выполните SQL-запрос
			cur.execute(update_sql, (ligaPoints, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")

	@dp.callback_query(F.data == "one")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 1 LigaPoint')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print(row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  ligaPoints = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			ligaPoints = str(int(nick + 1))

			# Выполните SQL-запрос
			cur.execute(update_sql, (ligaPoints, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")


	@dp.callback_query(F.data == "vibor")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 10 LigaPoint')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print(row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  ligaPoints = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			ligaPoints = str(int(nick + 10))

			# Выполните SQL-запрос
			cur.execute(update_sql, (ligaPoints, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")

	@dp.callback_query(F.data == "star5")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 5 Rep')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value = Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print("LigaPoint: ",row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  reput = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			# ligaPoints = str(int(nick + 5))
			reput = str(float((float(Rep) + 5.0) / 2.0))

			# Выполните SQL-запрос
			cur.execute(update_sql, (reput, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")


	@dp.callback_query(F.data == "star4")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 4 Rep')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print("LigaPoint: ",row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  reput = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			# ligaPoints = str(int(nick + 5))
			reput = str(float((float(Rep) + 4.0) / 2.0))

			# Выполните SQL-запрос
			cur.execute(update_sql, (reput, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")

	@dp.callback_query(F.data == "star3")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 3 Rep')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print("LigaPoint: ",row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  reput = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			# ligaPoints = str(int(nick + 5))
			reput = str(float((float(Rep) + 3.0) / 2.0))

			# Выполните SQL-запрос
			cur.execute(update_sql, (reput, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")



	@dp.callback_query(F.data == "star2")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 2 Rep')

		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print("LigaPoint: ",row[4])
		else:
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  reput = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			# ligaPoints = str(int(nick + 5))
			reput = str(float((float(Rep) + 2.0) / 2.0))

			# Выполните SQL-запрос
			cur.execute(update_sql, (reput, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")


	@dp.callback_query(F.data == "star1")
	async def call_finish(callback: types.CallbackQuery):
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f'Вы начислили 1 Rep')
		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		table_name = "ligatable"
		nickname_value =  Main_list[-1]

		# SQL-запрос для выборки строки по nickname
		sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

		# Выполнение SQL-запроса
		cur.execute(sql, (nickname_value,))

		# Получение результатов запроса
		row = cur.fetchone()

		# Печать строки
		if row:
			print("Вся строка:")
			global nick
			global Rep
			nick = row[4]
			Rep = row[5]
			print(row[4])
		else:
			
			await callback.message.answer(f"Такого nickname нету, посмотрите правильность ввода")

		get_id_sql = "SELECT ligatable_id FROM ligatable WHERE nickname = %s"
		nickname = Main_list[-1]  # Укажите нужный nickname здесь
		cur.execute(get_id_sql, (nickname,))
		row = cur.fetchone()

		if row:
			ligatable_id = row[0]

			# SQL-запрос для обновления данных
			update_sql = "UPDATE ligatable SET  reput = %s WHERE ligatable_id = %s"

			# Значения, которые вы хотите вставить в таблицу
			# ligaPoints = str(int(nick + 5))
			reput = str(float((float(Rep) + 1.0) / 2.0))

			# Выполните SQL-запрос
			cur.execute(update_sql, (reput, ligatable_id))

			# Закройте курсор и выполните коммит, чтобы изменения вступили в силу
			conn.commit()
			cur.close()
			conn.close()
		else:
			print("Информация по данному nickname не найдена.")
		

	@dp.callback_query(F.data == "add")
	async def call_finish(callback: types.CallbackQuery):
		conn = psycopg2.connect(
			dbname="robodendim",
			user="robodendim",
			password="Darawes228",
			host="pg3.sweb.ru",
			port="5432"
		)
		cur = conn.cursor()
		first_name = Main_list[0]
		last_name = Main_list[1]
		nickname = Main_list[-1]
		LigaPoints = 0
		Reput = 5.0
		cur.execute("INSERT INTO ligatable (first_name, last_name, nickname, ligaPoints, reput) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, nickname, str(LigaPoints), str(Reput)))

		# Подтверждение изменений и закрытие соединения
		conn.commit()
		cur.close()
		conn.close()
		await callback.message.answer("Вы успешно записаны😇\nСпасибо что воспользовались ботом")
		await boty.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)
		await callback.message.answer(f"{callback.message.from_user.first_name}\nВыберите действие:", reply_markup=get_keyboard())
		Main_list.clear()


	@dp.message()
	async def list_add(message: types.Message):
		global res
		res = poisk(str(message.text))
		global mess
		mess = []
		mess.clear
		mess = message.text.split()
		print(mess)
		print(message.text)
		Main_list.append(message.text)
		# mess = Main_list[-1]
		await message.answer(f'Вы записали: {Main_list}')
		# await message.answer(f'Записал\nНажмите следующую кнопку или если нужно найти',reply_markup=get_poisk())


	# @dp.callback_query(F.data == "poisk")
	# async def call_finish(callback: types.CallbackQuery):
	# 	my_list = res.split()
	# 	await callback.message.answer(f'Пользователь:\n<{my_list[0]} {my_list[1]} {my_list[2]}>\n💰LigaPoints: {my_list[3]}💰\n🟢Порядочность: {my_list[-1]}🔴')
	
		


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    logging.basicConfig(level=logging.INFO)
    # And the run events dispatching
	# subprocess.run(["python", "Liga2bot.py"])
    await dp.start_polling(boty, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
	print("start")
	# subprocess.run(["python", "Liga2bot.py"])
	asyncio.run(main())