import os

os.system('cls')


class User:
    name = None
    age = None
    user_id = None

Us_id = 0

Daniel = User()
Daniel.name = input('Введите имя: ')
Daniel.age = int(input("Введите ваш возраст: "))
Daniel.user_id = Us_id + 1


print(Daniel.name)
print(Daniel.age)
print(Daniel.user_id)