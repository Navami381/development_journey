credit_score=int(input("enter credit score="))

if credit_score>=800 and credit_score<=850:
    print("excellent")
elif credit_score>=740 and credit_score<=799:
    print("very good")
elif credit_score>=670 and credit_score<=739:
    print("good")
elif credit_score>=580 and credit_score<=669:
    print("fair")
else: 
    print("poor")
