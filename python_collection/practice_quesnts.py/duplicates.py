"""
write a program to print duplicate numbers

    arr=[10,1,15,16,11,10,12,11]

    o/p => [10,11]
"""
arr=[10,1,15,16,11,10,12,11]

duplicates=set()

for num in arr:
    if arr.count(num)>1:
     duplicates.add(num)
print(duplicates)

