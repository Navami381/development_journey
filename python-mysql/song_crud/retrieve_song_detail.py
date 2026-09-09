from mysql import connector

#step 2 :establish connection

connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="song_db"
)

#create cursor object
cursor=connection.cursor()

query="select * from song where id=%s"
values=(2,)             #always tuple because cant modify
cursor.execute(query,values)
record=cursor.fetchone()
print(record)