"""
Convert all names to uppercase Input:
    names=[“john”,“alice”,“bob”,“emma”] Output:
    [“JOHN”,“ALICE”,“BOB”,“EMMA”]
"""
names=["john","alice","bob","emma"]
uppercase=[w.upper() for w in names ]
print(uppercase)