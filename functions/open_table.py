import tkinter as tk
from functions import update_table
from tkinter import ttk

def open_table():
    try:
        table = tk.Tk()
        table.title("Таблица")
        table.attributes("-topmost",True)
        table.iconbitmap(f'icons/table.ico')
        table.resizable(False,False)
        

        columns = ("name", "price", "author")

        tree = ttk.Treeview(table ,columns=columns, show="headings", )
        tree.grid(row=0, column=0)

    
        tree.heading("name", text="Name", anchor="w")
        tree.heading("price", text="Price", anchor="w")
        tree.heading("author", text="Author", anchor="w")
    
        people = update_table.upd_table()
        for person in people:
            tree.insert("", tk.END, values=person)


        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="nswe")
    except Exception as e:
        pass
    finally:
        pass