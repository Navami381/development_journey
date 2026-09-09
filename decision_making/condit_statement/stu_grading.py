"""
**Student Grading**:
   - Marks ≥ 90: Grade A
   - Marks ≥ 75: Grade B
   - Marks ≥ 50: Grade C
   - Otherwise: Fail

"""
marks=int(input("enter marks: "))

if marks>=90:
    print("A GRADE")
elif marks>=75:
    print("B GRADE")
elif marks>=50:
    print("C GRADE")
else:
    print("fail")