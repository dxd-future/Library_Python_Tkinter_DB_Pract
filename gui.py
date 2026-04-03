import tkinter as tk
from functions import open_table, add_book, edit_book_window

def add():
    add_book.add_book(name_input.get(), price_input.get(), author_input.get())
    name_input.delete(0, tk.END)
    price_input.delete(0, tk.END)
    author_input.delete(0, tk.END)

def open_edit_window():
    edit_book_window.open_edit_window()

root = tk.Tk()

root.title("Библиотека")    
root.geometry("350x400")
root.resizable(False, False)
root.iconbitmap(f'icons/books_3025.ico')


open_table_button = tk.Button(root, text="Показать таблицу", background="#ffffff", border=1, width=20, height=1, font=("Arial", 14),command=open_table.open_table)
open_table_button.pack(anchor="center", pady=2)


frame = tk.Frame(root, bd=2, relief=tk.RAISED)
frame.pack(fill="both", expand=True, padx=10, pady=10)

label = tk.Label(frame, text="Добавление книги", font=("Arial", 20))
label.pack(pady=10)

label = tk.Label(frame, text="Введите название книги", font=("Arial", 14))
label.pack(anchor="center")
name_input = tk.Entry(frame, width=20, font=("Arial", 12))
name_input.pack(anchor="center", pady=10)

label = tk.Label(frame, text="Введите цену книги", font=("Arial", 14))
label.pack(anchor="center")
price_input = tk.Entry(frame, width=20,  font=("Arial", 12))
price_input.pack(anchor="center", pady=10)

label = tk.Label(frame, text="Введите автора книги", font=("Arial", 14))
label.pack(anchor="center")  
author_input = tk.Entry(frame, width=20, font=("Arial", 12))
author_input.pack(anchor="center", pady=10)

add_book_button = tk.Button(frame, text="Добавить книгу", font=("Arial", 12), background="#6bff6b", command=add)
add_book_button.pack(anchor="center", pady=5)

root.mainloop()