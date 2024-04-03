import mysql.connector


db = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='client'
    )

cursor = db.cursor()


sql = "INSERT INTO people (name, user_id) VALUES (%s, %s)"
val = ("test_name", 12314)
cursor.execute(sql, val)
db.commit()

print(cursor.rowcount, "запись добавлена")