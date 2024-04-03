import datetime
from datetime import datetime, timedelta
# Получаем текущую дату
current_date = datetime.now()
# Получаем дату следующего месяца
future_date = current_date + timedelta(days=30)
# Форматируем дату в нужном формате
formatted_date_day = current_date.strftime("%d")
formatted_future_day = future_date.strftime("%d")
formatted_date_moth = current_date.strftime("%m")
formatted_future_date = future_date.strftime("%m")
#formatted_date_moth = '01'
formatted_date_moth = int(formatted_date_moth)
formatted_future_date = int(formatted_future_date)
#print(formatted_date_moth)

def proverka(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        # Для февраля нужна дополнительная проверка на високосный год
        if (current_date.year % 4 == 0 and current_date.year % 100 != 0) or (current_date.year % 400 == 0):
            return 29
        else:
            return 28

#print(proverka(formatted_date_moth))
#print(proverka(formatted_future_date))
#print(formatted_date_day)
#print(formatted_future_day)