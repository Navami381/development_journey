"""
 Extract words longer than 5 letters Input:
    words=[“apple”,“watermelon”,“dog”,“elephant”,“cat”] Expected Output:
    [“watermelon”,“elephant”]
"""
words=["apple","watermelon","dog","elephant","cat"]
longer_than_five=[w for w in words if len(w)>5]
print(longer_than_five)