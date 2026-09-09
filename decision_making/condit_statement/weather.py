"""
**Weather Conditions**:
   - Above 30: Hot
   - 20 to 30: Warm
   - Below 20: Cold
"""
wthr=int(input("enter temperature"))

if wthr>30:
    print("hot")
elif wthr>=20 and wthr<=30:
    print("warm")
else:
    print("cold")

