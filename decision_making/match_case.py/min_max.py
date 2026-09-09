num1=int(input("enter number1..."))
num2=int(input("enter number2..."))

optn=input("enter min or max=")

match optn:

    case "min":
        if num1<num2:
            print("minimum is mum1",num1)
        else:
            print("minimum is num2",num2)
    case "max":
        if num1>num2:
            print("maximum is mum1",num1)
        else:
            print("maximum is num2",num2)
    case _ :
        print("invalid")