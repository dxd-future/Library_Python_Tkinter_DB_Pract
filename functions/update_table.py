from functions import contact

def upd_table():
    connection = contact.connection_pool.getconn()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT name,price,author FROM books')
        records = cursor.fetchall() 
        return records
    except Exception as e:
        print(Exception)
    finally:
        pass