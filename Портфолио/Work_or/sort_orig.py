import re
import json
from datetime import datetime

def calculate_race_times(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.split()
            numbers = [int(num) for num in re.findall(r'\d+', line)]
            val1 = columns[2]
            
            for line in file:
                columns = line.split()
                numbers = [int(num) for num in re.findall(r'\d+', line)]
                val2 = columns[2]
                
                start = datetime.strptime(val1.replace(',', '.'), "%H:%M:%S.%f")
                end = datetime.strptime(val2.replace(',', '.'), "%H:%M:%S.%f")
                time_difference = abs(end - start)
                keys = numbers[0]
                
                with open('sorted_times.txt', 'a+', encoding='utf-8') as f:
                    f.write(f"{columns[0]} {columns[1]} {time_difference}\n")
                print("Разница во времени:", time_difference)
                break

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
                f.write(line.replace('.', ','))

# Example Usage
# input_file = 'results_RUN copy.txt'
# output_file = 'sorted_times.txt'
# calculate_race_times(input_file, output_file)
# sort_times(output_file)