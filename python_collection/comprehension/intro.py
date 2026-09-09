arr=[2,3,4,5,6]
squares=[num**2 for num in arr]
print(squares)

cube=[num**3 for num in arr]
print(cube)

add_five=[num+5  for num in arr]
print(add_five)

evens=[num for num in arr if num%2==0]
print(evens)

odd=[num for num in arr if num%2!=0]
print(odd)