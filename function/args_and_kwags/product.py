def product(*args):
    product=1
    for i in args:
        product=product*i

    return product


print(product(3,7))
print(product(3,7,5))