"""
ADD:
append(value)= add object at end of list
insert(value,index)= inserts value at specific index

REMOVE:
pop(index): removes object from specific index, default index=-1
remove(value): removes first ocuurence of object

index(value)= returns index of first occurence of value
count(value)= returns frequency of value
reverse()= reverse the list
sort()= sorts the list
copy()= creates a copy of the list. but it will point to a different object

"""
expenses=[12000,110000,15000,16000,13000,17000]
#           0    1      2       3     4
march_month_exp=expenses[2]

print(march_month_exp)

expenses[0]=15000   #update jan month exp as 15000

print(expenses)

#display all amount one by one
#index
print("using index.........")
for i in range(0,len(expenses)):

    print(expenses[i])

print("using in.........")
for amount in expenses:

    print(amount)
    