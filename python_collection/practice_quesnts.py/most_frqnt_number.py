"""
)write a program to print most frequent  number

     arr=[10,1,15,16,11,10,12,11,12,18,12]
    
    o/p => 12
"""
arr=[10,1,15,16,11,10,12,11,12,18,12]

most_frequent=arr[0]

for num in arr:

    if arr.count(num)>arr.count(most_frequent):

        most_frequent=num

print(most_frequent)