class Number:
    def odd_even(self, num):
        if num % 2==0:
            print(num, "is Even")
        else:
            print(num, "is Odd")


num_instance = Number()
num_instance.odd_even(10)
num_instance.odd_even(7)