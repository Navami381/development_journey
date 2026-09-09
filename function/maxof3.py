def max_of_3(num1,num2,num3):

    if num1>num2 and num1>num3:
        print("num1 is larger=",num1)

    elif num2>num1 and num2>num3:
        print("num2 is larger=",num2) 
    
    elif num3>num1 and num3>num2:
        print("num3 is larger=",num3) 

    else:
        print("invalid")

max_of_3(7,5,22)
max_of_3(10,5,2)
max_of_3(6,20,10)
