def armstrong(number):

    org_number = number
    digit_count = len(str(number))
    total = 0

    while number != 0:
        digit = number % 10
        exponent = digit ** digit_count
        total = total + exponent
        number = number // 10

    if total == org_number:
        print(org_number, "is an ARMSTRONG NUMBER")
    else:
        print(org_number, "is NOT an ARMSTRONG NUMBER")

    print("Sum =", total)


armstrong(153)
armstrong(223)
armstrong(445)