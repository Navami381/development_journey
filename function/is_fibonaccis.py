def fibonacci(number):

    first=0 
    second=1
    next=1
    
    while next<=number:
    
        next=first+second

        if next==number:

            print(True)
            break
        first=second

        second=next

    else:

            print(False)
    
        
fibonacci(24)
fibonacci(21)
