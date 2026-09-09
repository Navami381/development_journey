def fibonacci(number):

    f=0 

    s=1

    for i in range(1,number+1):

        print(f)

        n=f+s

        f=s

        s=n
        
fibonacci(10)
