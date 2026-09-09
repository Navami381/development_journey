class Factorial:


    def factorial(self,number):

        result=1

        for i in range(1,number+1):

            result=result*i

        print(result)   
        
fact_instance=Factorial()
fact_instance.factorial(4)
fact_instance.factorial(8)
