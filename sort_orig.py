import re
from datetime import datetime

# В кратце в функции я нахожу промежуток во времени
def calculate_race_times(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.split()
            # Это я сделал чтоб считывать только цифры, в номерном знаке
            # Просто я дурак открывал файл без encoding='utf-8', и не понимал что за херню он выдаёт xD
            numbers = [int(num) for num in re.findall(r'\d+', line)]
            val1 = columns[2]
            
            for line in file:
                columns = line.split()
                # Эта тема не нужна оставил просто на память о затупе xD
                numbers = [int(num) for num in re.findall(r'\d+', line)]
                val2 = columns[2]
                
                # replace, чтоб потом мне удобнее было выводить до 2 знаков после запятой, .2f короче
                start = datetime.strptime(val1.replace(',', '.'), "%H:%M:%S.%f")
                end = datetime.strptime(val2.replace(',', '.'), "%H:%M:%S.%f")
                # Как раз таки раздница во времени
                time_difference = abs(end - start)
                keys = numbers[0]
                
                with open('sorted_times.txt', 'a+', encoding='utf-8') as f:
                    f.write(f"{columns[0]} {columns[1]} {time_difference}\n")
                # Для себя)
                # print("Разница во времени:", time_difference)
                break

# Тут сортирую время по убыванию
def sort_times(input_file):
    import datetime
    with open(input_file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
    
        date_objects = []
        for line in lines:
            time_str = line.split(' ')[-1].strip()
            time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S.%f')
            date_objects.append((time_obj, line))
        
        date_objects.sort(key=lambda x: x[0])
        
        with open(input_file, 'w', encoding='utf-8') as f:
            for _, line in date_objects:
                # Возвращаю запятую)
                f.write(line.replace('.', ','))
