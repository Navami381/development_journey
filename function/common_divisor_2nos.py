def common_divisor_n(number1,number2):

    for i in range(1, min(number1, number2) + 1):

        if number1%i==0 and number2%i==0:

            print(i)

common_divisor_n(10,20)
common_divisor_n(50,30)