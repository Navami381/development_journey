"""
Replace empty strings with “Unknown”
    Input:[“John”,““,”Alice”,““,”David”]
    Output:[“John”,“Unknown”,“Alice”,“Unknown”,“David”]
"""
names=["John","","Alice","","David"]

result=["unknown" if len(n)==0 else n for n in names]

print(result)
