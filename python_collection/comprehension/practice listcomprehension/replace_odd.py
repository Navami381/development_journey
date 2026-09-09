# lv1 3 replace odd nos with odd
#LEVEL 3 1. Replace odd numbers with “Odd” Input:[2,5,8,7,10]
#Output:[2,“Odd”,8,“Odd”,10]


numbers=[2,5,8,7,10]
result=["odd" if num%2!=0 else num for num in numbers ]
print(result)