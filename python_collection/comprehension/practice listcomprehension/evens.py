"""
LEVEL 2 1. Extract even numbers Input: numbers=[3,8,15,22,10,5] Expected
Output: [8,22,10]
"""
numbers=[3,8,15,22,10,5]
even=[num for num in numbers if num%2==0]
print(even)