yr=int(input("enter a year"))

if yr%100!=0  and yr%4==0 : 
    print("leap year")
elif yr%100==0 and yr%400==0:
    print("leap year")
else:
    print("not leap year")

