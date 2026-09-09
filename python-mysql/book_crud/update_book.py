from mysql import connector

connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)
cursor=connection.cursor()

query="update  book set title=%s,author=%s,published_year=%s where id=%s"
values=("The Power of Now","Eckhart Tolle",1997,3)
cursor.execute(query,values) 
connection.commit()
print("record has been updated...")
