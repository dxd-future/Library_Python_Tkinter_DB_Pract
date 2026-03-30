import tkinter as tk
from functions import update_table, open_table, add_book

def add():
    add_book.add_book(name_input.get(), price_input.get(), author_input.get())
    name_input.delete(0, tk.END)
    price_input.delete(0, tk.END)
    author_input.delete(0, tk.END)


root = tk.Tk()

root.title("Библеотека")    
root.resizable(False, False)
root.state('zoomed') 
root.iconbitmap(f'icons/books_3025.ico')


open_table_button = tk.Button(root, text="Показать таблицу", command=open_table.open_table)
open_table_button.pack(anchor="center")

label = tk.Label(root, text="Введите название книги", font=("Arial", 14))
label.pack(pady=5)
name_input = tk.Entry(root, width=20)
name_input.pack(padx=5, pady=5)

label = tk.Label(root, text="Введите цену книги", font=("Arial", 14))
label.pack(pady=5)
price_input = tk.Entry(root, width=20)
price_input.pack(padx=5, pady=5)

label = tk.Label(root, text="Введите автора книги", font=("Arial", 14))
label.pack(pady=5)  
author_input = tk.Entry(root, width=20)
author_input.pack(padx=5, pady=5)

add_book_button = tk.Button(root, text="Добавить книгу", command=add)
add_book_button.pack(anchor="center")

root.mainloop()