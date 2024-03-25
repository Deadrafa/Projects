import json
import re

# Тут как раз открываю 2 файла input_json_file пользователя и мой созданный ранее sorted_times.txt
def process_files(input_json_file, input_text_file):
    with open(input_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with open(input_text_file, 'r', encoding='utf-8') as f, open('output_data.txt', 'a', encoding='utf-8') as output_files:
        for line in f:
            columns = line.split()  # Разбиваем строку на столбцы
            numbers = [int(num) for num in re.findall(r'\d+', line)]
            val1 = columns[2]
            kiss = numbers[0]
            # print(columns[2])
            
            # Ищет номерной знак, чтобы не вывести ноунеёмов 
            for key, value in data.items():
                # Чтобы мог обработать int(key_digits) а то он жаловался что это строка
                key_digits = re.sub(r'\D', '', key)
                if int(key_digits) == kiss:
                    new_data = f"{kiss} {value['Surname']} {value['Name']} {val1}\n"
                    # print("Это", new_data)
                    # В свой файл мучу результаты output_data.txt
                    output_files.write(new_data)