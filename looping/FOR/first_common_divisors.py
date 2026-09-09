"""
display first divisor of a number other than 1

"""
number=int(input("enter a number="))

for i in range(2,number+1):
    
    if(number%i==0):
    
     print(i)

     break


