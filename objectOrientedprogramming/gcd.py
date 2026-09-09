class Gcd:

 def gcd(self,number):

        gcd=1

        for i in range(2,number):

            if(number%i==0):

                gcd=i

        print("gcd of",number,"=",gcd)

gcd_instance=Gcd()
gcd_instance.gcd(8)
gcd_instance.gcd(16)
gcd_instance.gcd(7)