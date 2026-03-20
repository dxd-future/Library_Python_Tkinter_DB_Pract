from functions import contact

def add_book(name, price, author):
    connection = contact.connection_pool.getconn()
    cursor = connection.cursor()
    try: 
        query = "INSERT INTO users (login, password, mail) VALUES (%s,%s,%s); "
        params = (name,price,author)
        cursor.execute(query, params)
        connection.commit() 
        return "Отлично!"   
    except Exception as e:
        return e
    finally: 
        if connection: 
            cursor.close() 
            contact.connection_pool.putconn(connection) 
            contact.connection_pool.closeall()