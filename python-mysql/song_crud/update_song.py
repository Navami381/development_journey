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
update song set title=%s,movie=%s where id=%s
"""
values=("aradhike","ambili",1) #always tuple because cant modify
cursor.execute(query,values)
connection.commit()
print("record has been updated...")
