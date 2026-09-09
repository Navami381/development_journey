def min_of_three(num1, num2, num3):

    if num1 <= num2 and num1 <= num3:
        print(num1)
    elif num2 <= num1 and num2 <= num3:
        print(num2)
    else:
        print(num3)

min_of_three(30, 10, 20)
min_of_three(50, 1, 20)