#daily calories consumed

daily_calories={"mon":1000,"tue":2100,"wed":5000,"thur":2100,"fri":3000} #duplicate key not allowed
print(daily_calories)

fri_calories=daily_calories["fri"]

print("friday calorie=",fri_calories)

daily_calories["tue"]=6000   #can update value 
print(daily_calories)

