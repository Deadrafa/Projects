import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
from aiogram.enums import ParseMode
import sic2
import psycopg2


# conn = psycopg2.connect(
#     dbname="robodendim",
#     user="postgres",
#     password="lera228den",
#     host="localhost",
#     port="5432"
# )
# cur = conn.cursor()

TOKEN = ""

boty2 = Bot(token=sic2.TOKEN)
dd = Dispatcher()

User_List = {'Dead': FSInputFile('avatar.jpg'),
			 'avatar2': FSInputFile('avatar.jpg')}

kb_us = [
           [types.KeyboardButton(text="📊Посмотреть рейтинг📊")]
		   ]
Keyboard_US = types.ReplyKeyboardMarkup(keyboard=kb_us,resize_keyboard=True)


@dd.message(CommandStart())
async def process_start_command(message: types.Message):
	await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=Keyboard_US)
	



@dd.message(F.text =="📊Посмотреть рейтинг📊")
async def yslyga(message: types.Message):
	await boty2.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
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
			await boty2.send_photo(chat_id=message.from_user.id,photo=User_List['Dead'],caption=
						  	f"🏆 <b>Место:</b> {i} 🏆\n"
							f"🔵 <b>Имя:</b> {row[1]} 🔵\n"
							f"🟣 <b>Фамилия:</b> {row[2]} 🟣\n"
							f"⚪ <b>Ник:</b> {row[3]} ⚪\n"
							f"🛒 <b>LigaPoint:</b> {row[4]} 🛒\n"
							f"✅ <b>Rep:</b> {row[5]} ❌",
				 	parse_mode=ParseMode.HTML)
			i += 1
		else:
			await message.answer(f"🏆 <b>Место:</b> {i} 🏆\n"
							f"🔵 <b>Имя:</b> {row[1]} 🔵\n"
							f"🟣 <b>Фамилия:</b> {row[2]} 🟣\n"
							f"⚪ <b>Ник:</b> {row[3]} ⚪\n"
							f"🛒 <b>LigaPoint:</b> {row[4]} 🛒\n"
							f"✅ <b>Rep:</b> {row[5]} ❌",
				 	parse_mode=ParseMode.HTML)
			i += 1
		# print(row)

	# закрываем соединение
	conn.close()
		


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    logging.basicConfig(level=logging.INFO)
    # And the run events dispatching
    await dd.start_polling(boty2, allowed_updates=dd.resolve_used_update_types())

if __name__ == "__main__":
	print("start")
	asyncio.run(main())