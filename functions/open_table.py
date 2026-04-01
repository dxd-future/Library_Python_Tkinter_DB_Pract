import tkinter as tk
from functions import update_table, edit_book_window
from tkinter import ttk

def open_table():
    try:
        table = tk.Tk()
        table.title("Таблица")
        table.attributes("-topmost", True)
        table.iconbitmap(f'icons/table.ico')
        table.resizable(False, False)
        
        columns = ("id", "name", "price", "author")

        tree = ttk.Treeview(table, columns=columns, show="headings", height=20)
        tree.grid(row=0, column=0, padx=10, pady=10)
        
        tree.heading("id", text="ID", anchor="w")
        tree.heading("name", text="Название", anchor="w")
        tree.heading("price", text="Цена", anchor="w")
        tree.heading("author", text="Автор", anchor="w")
        tree.column("id", width=50)
        tree.column("name", width=200)
        tree.column("price", width=100)
        tree.column("author", width=150)

        scrollbar = ttk.Scrollbar(table, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns", pady=10)
    
        def load_data():

            for item in tree.get_children():
                tree.delete(item)
            

            people = update_table.upd_table()
            for person in people:
                tree.insert("", tk.END, values=person)
        

        load_data()
        

        def edit_selected():
            selected = tree.selection()
            if selected:
                item = tree.item(selected[0])
                values = item['values']
                if values:
                    edit_book_window.open_edit_window_with_data(
                        values[0], values[1], values[2], values[3], load_data
                    )
            else:
                tk.messagebox.showwarning("Предупреждение", "Выберите запись для редактирования!")
        

        def delete_selected():
            selected = tree.selection()
            if selected:
                if tk.messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить эту книгу?"):
                    item = tree.item(selected[0])
                    values = item['values']
                    if values:
                        book_id = values[0]
                        from functions import delete_book
                        delete_book.delete_book(book_id)
                        load_data()  
            else:
                tk.messagebox.showwarning("Предупреждение", "Выберите запись для удаления!")
        

        button_frame = tk.Frame(table)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        edit_btn = tk.Button(button_frame, text="Редактировать", background="#6bff6b", command=edit_selected, width=15)
        edit_btn.pack(side=tk.LEFT, padx=5)
        
        delete_btn = tk.Button(button_frame, text="Удалить", background="#ff7d7d", command=delete_selected, width=15)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        refresh_btn = tk.Button(button_frame, text="Обновить", background="#7474ff", command=load_data, width=15)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
    except Exception as e:
        print(f"{e}")
