"""
**Ticket Fare**
   - Age < 5: Free
   - Age 5 – 18: ₹10
   - Age 19 – 60: ₹20
   - Age > 60: ₹15
"""
age=int(input("enter age..."))

if age<5:
    print("free")
elif age >=5 and age<=18:
    print("rs 10")
elif age>=19 and age<=60:
    print("rs 20")
else:
    print("rs 15")