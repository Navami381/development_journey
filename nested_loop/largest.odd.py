num=int(input("enter a number..."))

while num!=0:

    digit=num%10

    if digit%2!=0:
        print(num)
        break
    else:
        num=num//10
    