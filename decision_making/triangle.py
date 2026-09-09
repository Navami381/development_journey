a1=int(input("enter  angle 1="))

a2=int(input("enter angle 2="))

a3=int(input("enter angle 3="))

if a1>0 and a2>0 and a3>0:

    if a1+a2+a3 == 180: 

     print("can form triangle")

    else:

      print("cant form triangle")
     
else:

      print("angle should be greater than 0")