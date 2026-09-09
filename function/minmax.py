def min_max(num1, num2):
    optn = input("Enter min or max: ")

    match optn:
        case "min":
            if num1 < num2:
                print("Minimum is num1:", num1)
            else:
                print("Minimum is num2:", num2)

        case "max":
            if num1 > num2:
                print("Maximum is num1:", num1)
            else:
                print("Maximum is num2:", num2)

        case _:
            print("Invalid option")

min_max(25,50)
min_max(100,50)
min_max(10,50)