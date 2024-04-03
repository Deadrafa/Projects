import csv
import time
import os
os.system('cls')

second = time.time()
#second = int(second)
last_four_digits = str(second)[-4:]
last_four = str(second)[+6:]
last_four = float(last_four)
last_four = int(last_four)
last_four_digits = int(last_four_digits)
#print(f'Это число после точки: {last_four_digits}\nЭто число до точки: {last_four}')
random = (last_four + last_four_digits) - (last_four  * 2)
#print(f'Это рандом: {random}')
user_list = []
a = 0

while a != 3:
    a +=1
    random += random
    user_list = random
    def random_omg():
        random = (last_four + last_four_digits) - (last_four  * 2)
        return random
    print(f'Это рандом: {random}')
print("\n")
print(f'Это список: {user_list}')

# Создание CSV-файла
with open('Testirovanie.csv', 'w', newline='') as csvfile:
    fieldnames = ['user_word', 'preds']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'user_word': 'Daniil', 'preds': f'{random_omg()}'})
    writer.writerow({'user_word': 'Jane', 'preds': f'{random_omg()}'})
    writer.writerow({'user_word': 'John', 'preds': f'{random_omg()}'})
    writer.writerow({'user_word': 'Lera', 'preds': f'{random_omg()}'})
    writer.writerow({'user_word': 'Lilo', 'preds': f'{random_omg()}'})
    writer.writerow({'user_word': 'Jeck', 'preds': f'{random_omg()}'})

# Чтение из CSV-файла
with open('Testirovanie.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['user_word'], row['preds'])




#print(f'{second:.20}')