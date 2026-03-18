from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool( 
1, 10, 
host="localhost", 
database="Library", 
user="postgres", 
password="root" 
)