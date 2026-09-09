number=int(input("enter a number..."))

org_number=number

digit_count=len(str(number))

total=0

while(number!=0):

    digit=number%10

    exponent=digit**digit_count

    total=total+exponent

    number=number//10

if total==org_number:

    print("ARMSTRONG NUMBER")

else:

    print("not an ARMSTRONG NUMBER")

print(total)