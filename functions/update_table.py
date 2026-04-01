from functions import contact
from tkinter import *

def upd_table():
    connection = contact.connection_pool.getconn()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT id, name, price, author FROM books ORDER BY id')
        records = cursor.fetchall() 
        return records     
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return []
    finally:
        if connection: 
            cursor.close() 
            contact.connection_pool.putconn(connection)