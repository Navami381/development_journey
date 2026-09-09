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

query="""
insert into song(title,track_number,movie,singers) values(%s,%s,%s,%s)
"""
values=('Darshana', 3, 'Hridayam', 'Hesham Abdul Wahab')
cursor.execute(query,values)
connection.commit()
print("record has been recorded...")