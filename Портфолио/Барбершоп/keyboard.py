from aiogram import types

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Мужская стрижка", callback_data="strilka_def")],
        [
            types.InlineKeyboardButton(text="Фэйд", callback_data="feid")],
        [
            types.InlineKeyboardButton(text="Стрижка машинкой", callback_data="ctrijkaMashinkoi")],
        [
            types.InlineKeyboardButton(text="Детская стрижка\n(До 14 лет)", callback_data="kids_strichka")],
        [
            types.InlineKeyboardButton(text="Стрижка бороды", callback_data="boroda_strich")],
        [
            types.InlineKeyboardButton(text="Камуфляж головы", callback_data="golova_kamyflij")],
        [
            types.InlineKeyboardButton(text="Камуфляж бороды", callback_data="boroda_kamyflij")],
        [
            types.InlineKeyboardButton(text="КОМПЛЕКС - голова+борода", callback_data="Kompleksiks")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_reply_keyboard_onOnehour():
    buttons1 = [
        [
            types.InlineKeyboardButton(text='10:00 - 11:00', callback_data="10:00 - 11:00"),
            types.InlineKeyboardButton(text='11:00 - 12:00', callback_data="11:00 - 12:00")],
        [
            types.InlineKeyboardButton(text='12:00 - 13:00', callback_data="12:00 - 13:00"),
            types.InlineKeyboardButton(text='13:00 - 14:00', callback_data="13:00 - 14:00")],
        [
            types.InlineKeyboardButton(text='14:00 - 15:00', callback_data="14:00 - 15:00"),
            types.InlineKeyboardButton(text='15:00 - 16:00', callback_data="15:00 - 16:00")],
        [
            types.InlineKeyboardButton(text='16:00 - 17:00', callback_data="16:00 - 17:00"),
            types.InlineKeyboardButton(text='17:00 - 18:00', callback_data="17:00 - 18:00")],
        [
            types.InlineKeyboardButton(text='18:00 - 19:00', callback_data="18:00 - 19:00"),
            types.InlineKeyboardButton(text='19:00 - 20:00', callback_data="19:00 - 20:00")],
        [
            types.InlineKeyboardButton(text='20:00 - 21:00', callback_data="20:00 - 21:00")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons1)
    return keyboard

def get_reply_keyboard_half_and_hour():
    buttons2 = [
        [
            types.InlineKeyboardButton(text='10:00 - 11:30', callback_data="12ed112d"),
            types.InlineKeyboardButton(text='11:30 - 13:00', callback_data="12d12dd1")],
        [
            types.InlineKeyboardButton(text='13:00 - 14:30', callback_data="12d12d2d1"),
            types.InlineKeyboardButton(text='14:30 - 16:00', callback_data="12d2d1d")],
        [
            types.InlineKeyboardButton(text='16:00 - 17:30', callback_data="12d12ddwd"),
            types.InlineKeyboardButton(text='17:30 - 19:00', callback_data="12d1wfad")],
        [
            types.InlineKeyboardButton(text='19:00 - 20:30', callback_data="12e1wdcac")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons2)
    return keyboard


def get_reply_keyboard_half_hour():
    buttons3 = [
        [
            types.InlineKeyboardButton(text='10:00 - 10:30', callback_data="12ed112d"),
            types.InlineKeyboardButton(text='10:30 - 11:00', callback_data="12d12dd1"),
            types.InlineKeyboardButton(text='11:00 - 11:30', callback_data="12d12d2d1")],
        [
            types.InlineKeyboardButton(text='11:30 - 12:00', callback_data="12d2d1d"),
            types.InlineKeyboardButton(text='12:00 - 12:30', callback_data="12d12ddwd"),
            types.InlineKeyboardButton(text='12:30 - 13:00', callback_data="12d1wfad")],
        [
            types.InlineKeyboardButton(text='13:00 - 13:30', callback_data="12e1wdcac"),
            types.InlineKeyboardButton(text='13:30 - 14:00', callback_data="1dw1dasd"),
            types.InlineKeyboardButton(text='14:00 - 14:30', callback_data="12eqwsqac")],
        [
            types.InlineKeyboardButton(text='14:30 - 15:00', callback_data="12eqwsqac"),
            types.InlineKeyboardButton(text='15:00 - 15:30', callback_data="12e1esca"),
            types.InlineKeyboardButton(text='15:30 - 16:00', callback_data="12e1esca")],
        [
            types.InlineKeyboardButton(text='16:00 - 16:30', callback_data="12eqwsqac"),
            types.InlineKeyboardButton(text='16:30 - 17:00', callback_data="12e1esca"),
            types.InlineKeyboardButton(text='17:00 - 17:30', callback_data="12e1esca")],
        [
            types.InlineKeyboardButton(text='17:30 - 18:00', callback_data="12eqwsqac"),
            types.InlineKeyboardButton(text='18:00 - 18:30', callback_data="12e1esca"),
            types.InlineKeyboardButton(text='18:30 - 19:00', callback_data="12e1esca")],
        [
            types.InlineKeyboardButton(text='19:00 - 19:30', callback_data="12eqwsqac"),
            types.InlineKeyboardButton(text='19:30 - 20:00', callback_data="12e1esca"),
            types.InlineKeyboardButton(text='20:00 - 20:30', callback_data="12e1esca")],
        [
            types.InlineKeyboardButton(text='20:30 - 21:00', callback_data="1edasfgdggws")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons3)
    return keyboard

def get_reply_keyboard_finish():
    buttons4 = [
        [types.InlineKeyboardButton(text='Записаться', callback_data="finish_reg")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons4)
    return keyboard

def get_reply_keyboard_finish1():
    buttons5 = [
        [types.InlineKeyboardButton(text='Записаться', callback_data="finish_reg1")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons5)
    return keyboard

def get_reply_keyboard_finish2():
    buttons6 = [
        [types.InlineKeyboardButton(text='Записаться', callback_data="finish_reg2")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons6)
    return keyboard

def get_reply_keyboard_MYSQL():
    buttons_sql = [
        [types.InlineKeyboardButton(text="💾Зарегестрироваться💾", callback_data="Registr_users")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons_sql)
    return keyboard