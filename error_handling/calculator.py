num1=int(input("enter number1.."))
num2=int(input("enter number2.."))

try:

    operation=input("select operation + - * /")

    result=0

    if operation=="+":
        print(num1+num2)
    elif operation=="-":
        print(num1-num2)
    elif operation=="*":
        print(num1*num2)
    elif operation=="/":
        print(num1/num2)
    else:
        print("invalid operation")
        
except Exception as e:
    print(e)

else:
    print(result)



