attendance=[1.-1,0,1,-1,1,-1,0,0]

#1=>p
#-1=>o
#0=>h

result=["p" if a==1 else "o" if a==-1 else "h" for a in attendance]

print(result)