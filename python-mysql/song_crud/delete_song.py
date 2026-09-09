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

query=" delete from song where id=%s"
values=(1,)
cursor.execute(query,values)
connection.commit()
print("record deleted...")