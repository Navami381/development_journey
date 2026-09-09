age=int(input("enter age..."))

if age<18:
    raise Exception("Invalid age")  #raise to throw custom error
else:
    print("Eligable for vote")