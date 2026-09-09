fw=open("prime_number.txt","w")

for num in range(50,101):

    for i in range(2,num):

       if num%i==0:

           break
    else:
        fw.write(str(num)+"\n")


