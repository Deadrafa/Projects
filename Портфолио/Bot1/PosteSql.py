import os
import psycopg2
from psycopg2 import sql


os.system('cls')


# Установите параметры подключения к вашей базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="robodendim",
	user="robodendim",
	password="Darawes228",
	host="pg3.sweb.ru",
	port="5432"
)

# Создайте объект курсора для выполнения SQL-запросов
cur = conn.cursor()

# # Здесь пример создания таблицы "employees"
# table_name = "LigaTable"
# create_table_query = sql.SQL("""
#     CREATE TABLE {} (
#         LigaTable_id SERIAL PRIMARY KEY,
#         first_name VARCHAR(50),
#         last_name VARCHAR(50),
#         nickname VARCHAR(50),
#         LigaPoints BIGINT CHECK (LigaPoints >= 0 AND LigaPoints <= 100000),
#         Reput FLOAT(10,1)
#     )
# """).format(sql.Identifier(table_name))

# # Выполните SQL-запрос для создания таблицы
# cur.execute(create_table_query)

# # Фиксируем изменения
# conn.commit()

# # Закройте объект курсора и соединение с базой данных
# cur.close()
# conn.close()


menu = int(input("Добавить пользователя: 1\nНачислить LigaPoint: 2\nНачислить репутацию: 3\nВывести всех пользователей: 4\nВведите одну из команд: "))


if menu == 5:
    table_name = "ligatable"
    create_table_query = sql.SQL("""
                                 CREATE TABLE {} (
                                 ligatable_id SERIAL PRIMARY KEY,
                                 first_name VARCHAR(50),
                                 last_name VARCHAR(50),
                                 nickname VARCHAR(50),
                                 LigaPoints BIGINT CHECK (LigaPoints >= 0 AND LigaPoints <= 100000),
                                 Reput DECIMAL(7,2)
                                 )
                                 """).format(sql.Identifier(table_name))

# Выполните SQL-запрос для создания таблицы
    cur.execute(create_table_query)

# Фиксируем изменения
    conn.commit()

# Закройте объект курсора и соединение с базой данных
    cur.close()
    conn.close()

elif menu == 4:
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables = cur.fetchall()

# Вывод списка таблиц
    for table in tables:
        print(table[0])

# Закрытие соединения с базой данных
        conn.close()

elif menu == 1:
    # Пример добавления пользователя в таблицу
    first_name = "Daniel"
    last_name = "svin"
    nickname = "Dead"
    LigaPoints = 15
    Reput = 5.0

    cur.execute("INSERT INTO ligatable (first_name, last_name, nickname, ligaPoints, reput) VALUES (%s, %s, %s, %s, %s)", (first_name, last_name, nickname, str(LigaPoints), str(Reput)))

# Подтверждение изменений и закрытие соединения
    conn.commit()
    cur.close()
    conn.close()

elif menu == 7:
    cur.execute('SELECT * FROM ligatable')

# получаем результат
    rows = cur.fetchall()
    for row in rows:
        print(row)

# закрываем соединение
        conn.close()


elif menu == 0:
    # Напишите SQL-запрос для обновления данных в таблице
    sql = "UPDATE ligatable SET ligaPoints = %s, reput = %s WHERE ligatable_id = %s"

    # Значения, которые вы хотите вставить в таблицу
    ligaPoints = str(123)
    reput = str(float((5.0 + 4.75) / 2.0))
    condition_value = "2" #Номер строки которую хочешь исправить

    # Выполните SQL-запрос
    cur.execute(sql, (ligaPoints, reput, condition_value))

    # Закройте курсор и выполните коммит, чтобы изменения вступили в силу
    conn.commit()
    cur.close()
    conn.close()

elif menu == 34:
    cur.execute("SELECT first_name, last_name, nickname, ligaPoints, reput FROM ligatable")

# Получить результаты запроса
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Закрыть курсор и соединение
    cur.close()
    conn.close()

elif menu == 11:
    cur.execute("SELECT * FROM ligatable ORDER BY ligaPoints DESC")

# Получить результаты запроса
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Закрыть курсор и соединение
    cur.close()
    conn.close()


elif menu == 33:
    cur.execute("SELECT ligaPoints FROM ligatable")

# Получаем результаты
    column_3_data = cur.fetchall()

    # Выводим данные из 3го столбца
    for row in column_3_data:
        print(row[0])

    # Закрываем курсор и соединение с базой данных
    cur.close()
    conn.close()  


elif menu == 77:
    table_name = "ligatable"
    nickname_value = "Bebra"

    # SQL-запрос для выборки строки по nickname
    sql = f"SELECT * FROM {table_name} WHERE nickname = %s"

    # Выполнение SQL-запроса
    cur.execute(sql, (nickname_value,))

    # Получение результатов запроса
    row = cur.fetchone()

    # Печать строки
    if row:
        print("Вся строка:")
        print(row[5])
    else:
        print("Строка с указанным nickname не найдена.")

    # Закрытие курсора и соединения
    cur.close()
    conn.close()
