"""
### 4. Oxygen Level (SpO2)
- ≥ 95: Normal
- 90 – 94: Mild Concern
- < 90: Critical
"""
level=int(input("enter oxygen level"))

if level>=95:
    print("NORMAL")
elif level>=90 and level<=94:
    print("mild concern")
else:
    print("critical")