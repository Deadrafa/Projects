import json
import re

def process_files(input_json_file, input_text_file):
    with open(input_json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with open(input_text_file, 'r', encoding='utf-8') as f, open('output_data.txt', 'a', encoding='utf-8') as output_files:
        for line in f:
            columns = line.split()  # Разбиваем строку на столбцы
            numbers = [int(num) for num in re.findall(r'\d+', line)]
            val1 = columns[2]
            kiss = numbers[0]
            print(columns[2])
            
            for key, value in data.items():  # Iterate through the data dictionary
                key_digits = re.sub(r'\D', '', key)
                if int(key_digits) == kiss:
                    new_data = f"{kiss} {value['Surname']} {value['Name']} {val1}\n"
                    print("Это", new_data)
                    output_files.write(new_data)

# process_files('competitors2.json', 'sorted_times.txt', 'output_data.txt')   