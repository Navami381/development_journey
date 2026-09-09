arr=[10,11,1,10,11,2,3]

unique_nos=[num for num in arr if arr.count(num)==1]
print(unique_nos)

duplicate={num for num in arr if arr.count(num)>1}
print(duplicate)