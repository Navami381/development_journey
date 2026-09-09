"""
**Exam Marks – Distinction**
   - Marks ≥ 40: Pass.
   - Marks ≥ 90: Distinction.
   - Else: Fail.
"""
marks=int(input("enter marks..."))

if marks>=90:
    print("distinction")
elif marks>=40:
    print("pass")
else:
    print("fail")