import tkinter as tk
from tkinter import messagebox
from functions import contact


def open_edit_window_with_data(book_id, name, price, author, refresh_callback=None):
    edit_window = tk.Tk()
    edit_window.title(f"Редактирование книги: {book_id}")
    edit_window.geometry("350x300")
    edit_window.resizable(False, False)
    edit_window.attributes("-topmost", True)
    
    tk.Label(edit_window, text=f"Редактирование книги (ID: {book_id})", font=("Arial", 14, "bold")).pack(pady=10)
    

    tk.Label(edit_window, text="Название книги:", font=("Arial", 12)).pack(pady=5)
    name_entry = tk.Entry(edit_window, width=30)
    name_entry.insert(0, name)
    name_entry.pack(pady=5)
    
  
    tk.Label(edit_window, text="Цена книги:", font=("Arial", 12)).pack(pady=5)
    price_entry = tk.Entry(edit_window, width=30)
    price_entry.insert(0, price)
    price_entry.pack(pady=5)
    

    tk.Label(edit_window, text="Автор книги:", font=("Arial", 12)).pack(pady=5)
    author_entry = tk.Entry(edit_window, width=30)
    author_entry.insert(0, author)
    author_entry.pack(pady=5)
    
    def save_changes():
        new_name = name_entry.get()
        new_price = price_entry.get()
        new_author = author_entry.get()
        
        if not new_name or not new_price or not new_author:
            messagebox.showwarning("Ошибка", "Заполните все поля!")
            return
        
        try:
            connection = contact.connection_pool.getconn()
            cursor = connection.cursor()
            
            query = "UPDATE books SET name = %s, price = %s, author = %s WHERE id = %s"
            params = (new_name, new_price, new_author, book_id)
            cursor.execute(query, params)
            connection.commit()
            
            messagebox.showinfo("Успех", "Книга успешно обновлена!")
            
            cursor.close()
            contact.connection_pool.putconn(connection)
            
            edit_window.destroy()
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"{e}")
    
    button_frame = tk.Frame(edit_window)
    button_frame.pack(pady=20)
    
    btn_save = tk.Button(button_frame, text="Сохранить", command=save_changes, width=10)
    btn_save.pack(side=tk.LEFT, padx=5)
    btn_cancel = tk.Button(button_frame, text="Отмена", command=edit_window.destroy, width=10)
    btn_cancel.pack(side=tk.LEFT, padx=5)

    edit_window.mainloop()