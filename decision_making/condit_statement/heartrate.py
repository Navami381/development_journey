"""
### 3. Heart Rate
- < 60: Low
- 60 – 100: Normal
- > 100: High
"""

rate=int(input("enter heart rate..."))

if rate<60:

    print("LOW")

elif rate>=60 and rate<=100:

    print("NORMAL")

else:
    
    print("HIGH")