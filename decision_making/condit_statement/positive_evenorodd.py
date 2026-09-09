"""
**Positive Number – Even or Odd** - Check if positive. If yes, check for even/odd. Else, state "Not a positive number."
"""
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Even number")
    elif num % 2 !=0:
        print("Odd number")
else:
    print("Not a positive number")