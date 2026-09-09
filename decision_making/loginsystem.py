"""
✅ 3. Login System with Password and OTP

Task:
Ask for password.

If password is correct:

Ask for OTP

If OTP is correct → "Login successful"

Else → "Incorrect OTP"


Else → "Incorrect password"

"""


db_password="navami"

db_otp=12345

password=input("enter password =")

if db_password==password:

    otp=int(input("enter otp="))

    if otp == db_otp:

        print("LOGIN SUCCESSFULL")

    else :

        print("incorrect otp")
else :
    
    print("invalid password")