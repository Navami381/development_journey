#>pip install mysql-connector-python
#step 1: import connector from mysql

from mysql import connector

#step 2 :establish connection

connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost"
)

print(connection)

