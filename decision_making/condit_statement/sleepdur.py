"""
### 5. Sleep Duration
- < 6: Sleep Deprived
- 6 – 8: Healthy Sleep
- > 8: Oversleeping
"""
dur=int(input("enter sleep duration..."))

if dur<6:
    print("sleep deprived")
elif dur>=6 and dur<=8:
    print("Healthy sleep")
else:
    print("oversleep")