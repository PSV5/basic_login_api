import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (username text, password text, date text)"
cursor.execute(create_table)

connection.commit()

connection.close()