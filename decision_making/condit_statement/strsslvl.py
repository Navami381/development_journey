"""
### 6. Stress Level (1-10)
- 1 – 3: Low Stress
- 4 – 6: Moderate Stress
- 7 – 10: High Stress
"""
str=int(input("enter stress level..."))

if str>=1 and str<=3:
    print("low stress")
elif str>=4 and str<=6:
    print("Moderate sleep")
else:
    print("high stress")