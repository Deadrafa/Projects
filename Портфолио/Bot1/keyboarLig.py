from aiogram import types

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="Добавить пользователя", callback_data="add_user")],
        [
            types.InlineKeyboardButton(text="Начислить LigaPoints", callback_data="LigaPoints")],
        [
            types.InlineKeyboardButton(text="Начислить Рейтинг Порядочности", callback_data="Reiting")
        ]

    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_keyboard2():
    buttons = [
        [
            types.InlineKeyboardButton(text="Имя", callback_data="name")],
        [
            types.InlineKeyboardButton(text="Фамилию", callback_data="second_name")],
        [
            types.InlineKeyboardButton(text="никнейм", callback_data="nickname")],
        [
            types.InlineKeyboardButton(text="Записать", callback_data="add")
        ]
    ]
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard2


def get_poisk():
    buttons = [
        [
            types.InlineKeyboardButton(text="Поиск", callback_data="poisk")
        ]
    ]
    poisk = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return poisk




def get_poisk2():
    buttons = [
        [
            types.InlineKeyboardButton(text="Начислить", callback_data="nalik")
        ]
    ]
    poisk = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return poisk

def get_poisk3():
    buttons = [
        [
            types.InlineKeyboardButton(text="Начислить", callback_data="anal")
        ]
    ]
    poisk = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return poisk


def get_keyboard3():
    buttons = [
        [
            types.InlineKeyboardButton(text="Фамилию", callback_data="second_name")
        ]
    ]
    keyboard3 = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard3




def get_Point():
    buttons = [
        [
            types.InlineKeyboardButton(text="1", callback_data="one")],
        [
            types.InlineKeyboardButton(text="2", callback_data="two")],
        [
            types.InlineKeyboardButton(text="3", callback_data="free")],
        [
            types.InlineKeyboardButton(text="4", callback_data="four")],
        [
            types.InlineKeyboardButton(text="5", callback_data="five")],
        [
            types.InlineKeyboardButton(text="Бонус 10", callback_data="vibor")
        ]
    ]
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard2



def get_Rep():
    buttons = [
        [
            types.InlineKeyboardButton(text="🌟", callback_data="star1")],
        [
            types.InlineKeyboardButton(text="🌟🌟", callback_data="star2")],
        [
            types.InlineKeyboardButton(text="🌟🌟🌟", callback_data="star3")],
        [
            types.InlineKeyboardButton(text="🌟🌟🌟🌟", callback_data="star4")],
        [
            types.InlineKeyboardButton(text="🌟🌟🌟🌟🌟", callback_data="star5")
        ]
    ]
    keyboard2 = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard2


def get_sort():
    buttons = [
        [
            types.InlineKeyboardButton(text="Сортировка по местам", callback_data="sort")
        ]
    ]
    poisk = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return poisk