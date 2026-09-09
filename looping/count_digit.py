number=int(input("enter a number..."))

count=0

while(number!=0):

    digit=number%10

    count+=1

    number=number//10

print(count)
