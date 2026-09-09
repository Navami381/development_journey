"""
 Extract names starting with ‘A’ Input:
    names=[“Alice”,“Bob”,“Andrew”,“Emma”,“Alex”] Expected Output:
    [“Alice”,“Andrew”,“Alex”]
"""
names=["Alice","Bob","Andrew","Emma","Alex"]
starts_with_a=[w for w in names if w.startswith("A")]
print(starts_with_a)