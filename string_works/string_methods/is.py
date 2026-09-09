password="password@123"

if password.isalpha():

    print("password is alphabet")

elif password.isdigit():

    print("password is digit")

elif password.isalnum():

    print("password is alphanumeric")

else:
    print("special character")

