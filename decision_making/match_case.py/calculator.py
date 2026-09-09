num1=int(input("enter number1..."))
num2=int(input("enter number2..."))

op=input("enter operator '+,-,*,/'=")

match op:

    case "+":
        print( "addition=",num1+num2)
    case "-":
        print( "substraction=",num1-num2)
    case "*":
        print( "multiplication=",num1*num2)
    case "/":
        print("division=", num1/num2)
   
    case _ :
        print( "invalid")
            