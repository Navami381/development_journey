from mysql import connector

connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)
cursor=connection.cursor()

query="select * from book"
cursor.execute(query) 
records=cursor.fetchall()
for book in records:
    print(book)