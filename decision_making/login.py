db_username="navami"

db_pin=12345

user_name=input("enter username =")

if db_username==user_name:

    password=int(input("enter password="))

    if password == db_pin:

        print("LOGIN SUCCESSFULL")

    else :

        print("password incorrect")
else :
    
    print("invalid username")