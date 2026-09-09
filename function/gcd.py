def gcd(number):

    for i in range(2,number):

        if(number%i==0):

            gcd=i

    print("gcd of",number,"=",gcd)

gcd(8)
gcd(16)
gcd(4)