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

query="select * from song"
cursor.execute(query)
records=cursor.fetchall()
for song in records:
    print(song)