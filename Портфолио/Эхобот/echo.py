import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import sic


TOKEN = ""
admin_id = '' 

boty = Bot(token=sic.TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: types.Message):
	if message.from_user.id == sic.admin_id:
		await message.answer(f"Hi, admin -_-")
	else:
		await message.answer(f"Привет, {message['from'].first_name}!")
		
@dp.message()
async def process_start_command(message: types.Message):
	if message.reply_to_message == None:
		if '/start' not in message.text:
			await boty.forward_message(sic.admin_id, message.from_user.id, message.message_id)
	else:
		if message.from_user.id == sic.admin_id:
			if message.reply_to_message.forward_from.id:
					await boty.send_message(message.reply_to_message.forward_from.id, message.text)
		else:
			await message.answer('Нельзя отвечать на сообщения.')

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    logging.basicConfig(level=logging.INFO)
    # And the run events dispatching
    await dp.start_polling(boty, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
	print("start")
	asyncio.run(main())
