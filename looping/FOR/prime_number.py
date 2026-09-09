"""

display first divisor of a number other than 1 and same number

"""
number=int(input("enter a number="))

for i in range(2,number):
    
    if(number%i==0):
    
      print("not prime number")

      break

else:
       
       print("prime number")