employe={"id":100,"name":"syam","dept":"hr"}

key=input("enter key...")

try :
    print(employe[key])
    
except Exception as e:
    print(e)

finally:
    print("db commit....")