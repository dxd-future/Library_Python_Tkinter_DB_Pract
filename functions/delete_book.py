from functions import contact
from tkinter import messagebox

def delete_book(book_id):
    try:
        connection = contact.connection_pool.getconn()
        cursor = connection.cursor()
        query = "DELETE FROM books WHERE id = %s"
        query2 = "SELECT setval('public.books_id_seq', (SELECT MAX(id) FROM books));"
        cursor.execute(query, (book_id,))
        cursor.execute(query2)
        connection.commit()
        
        messagebox.showinfo("Успех", "Книга успешно удалена!")
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"{e}")
        
    finally:
        if connection:
            cursor.close()
            contact.connection_pool.putconn(connection)