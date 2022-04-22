import datetime
import sqlite3

def previous_day_reg():
    previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
    previous_date = previous_date.strftime("%D")
    print(previous_date)

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    query = "SELECT username FROM users WHERE date=?"
    result = cursor.execute(query, (previous_date,))
    row = result.fetchall()
    if row:
        user = row
    else:
        user = None
    
    connection.close()
    return row

def send_mail(lst):
    pass

if __name__ == "__main__":
    prev = previous_day_reg()
    res = [item for t in prev for item in t]
    print(res)
