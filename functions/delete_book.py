from functions import contact
from tkinter import messagebox

def delete_book(book_id):
    try:
        connection = contact.connection_pool.getconn()
        cursor = connection.cursor()
        
        query = "DELETE FROM books WHERE id = %s"
        cursor.execute(query, (book_id,))
        connection.commit()
        
        messagebox.showinfo("Успех", "Книга успешно удалена!")
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"{e}")
        
    finally:
        if connection:
            cursor.close()
            contact.connection_pool.putconn(connection)