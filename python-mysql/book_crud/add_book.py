#create python mysql book crud application that include insert,list,retrieve,update,delete of book
from mysql import connector

connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)
cursor=connection.cursor()

query="""
insert into book(title,author,price,category,published_year) values(%s,%s,%s,%s,%s)
"""
values=('Harry Potter', 'J.K. Rowling', 550.00, 'Fantasy', 1997)
cursor.execute(query,values)
connection.commit()
print("record has been recorded...")
