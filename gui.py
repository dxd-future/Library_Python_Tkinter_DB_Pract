import tkinter as tk
from functions import update_table, open_table, add_book

root = tk.Tk()

root.title("Библеотека")    
root.resizable(False, False)
root.state('zoomed') 
root.iconbitmap(f'icons/books_3025.ico')


open_table_button = tk.Button(root, text="Показать таблицу", command=open_table.open_table)
open_table_button.pack(anchor="center")


update_table_button = tk.Button(root, text="Обновить таблицу", command=update_table.upd_table)
update_table_button.pack(anchor="center")


add_book_button = tk.Button(root, text="Добавить книгу", command=add_book.add_book)
add_book_button.pack(anchor="center")


root.mainloop()