from functions import contact
import tkinter as tk
from tkinter import messagebox

def add_book(name, price, author):
    if not name or not price or not author:
        messagebox.showwarning("Ошибка", "Заполните все поля!")
        return

    connection = contact.connection_pool.getconn()
    cursor = connection.cursor()
    try: 
        query = "INSERT INTO books (name, price, author) VALUES (%s, %s, %s);"
        params = (name, price, author)
        cursor.execute(query, params)
        connection.commit() 
        
        messagebox.showinfo(title="Таблица", message="Книга добавлена!")
        return "Отлично!"   
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось добавить: {e}")
        return e
    finally: 
        if connection: 
            cursor.close() 
            contact.connection_pool.putconn(connection)