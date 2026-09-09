sugarlvl=int(input("enter a number="))
if sugarlvl>300:
    print("very high")
elif sugarlvl>140 and sugarlvl<=220:
    print("high")
elif sugarlvl>90 and sugarlvl<=140:
    print("normal")
elif sugarlvl>80 and sugarlvl<=90:
    print("low")
else:
    print("very high")
