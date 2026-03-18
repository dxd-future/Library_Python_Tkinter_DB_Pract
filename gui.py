import tkinter as tk
from tkinter import ttk

from functions import update_table


root = tk.Tk()

root.title("Библеотека")    
root.resizable(False, False)
root.state('zoomed') 
root.iconbitmap(f'icons/books_3025.ico')


frame = tk.Frame(root, bg="#909090")
frame.pack(fill="x")

people = update_table.upd_table()

columns = ("name", "price", "author")

tree = ttk.Treeview(columns=columns, show="headings")
tree.grid(row=0, column=0)


tree.heading("name", text="Name", anchor="w")
tree.heading("price", text="Price", anchor="w")
tree.heading("author", text="Author", anchor="w")


for person in people:
    tree.insert("", tk.END, values=person)


scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="nswe")
 

    


root.mainloop()