from functions import contact
from tkinter import *
from tkinter.messagebox import showinfo

def upd_table():
    connection = contact.connection_pool.getconn()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT name,price,author FROM books')
        records = cursor.fetchall() 
        showinfo(title="Таблица", message="Таблица обновлена!")
        return records     
    except Exception as e:
        print(Exception)
    finally:
        if connection: 
            cursor.close() 
            contact.connection_pool.putconn(connection) 
            contact.connection_pool.closeall()