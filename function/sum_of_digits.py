def sum_of_digits(number):

    total = 0

    while number != 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    print(total)

sum_of_digits(123)
sum_of_digits(153)