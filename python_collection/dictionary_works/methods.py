"""define={key:value}
mutable:yes
duplicates: duplicate key not allowed

METHODS
keys() - return all keys
values()- return all values
items() - return all key and value
get(key) - gives value of the key, gives none if key doesn't exist
"""
daily_calories={"mon":1000,"tue":2100,"wed":5000,"thur":2100,"fri":3000} #duplicate key not allowed
print(daily_calories)

print("all keys.......")
for k in daily_calories.keys():
    print(k)

print("all values......")
for v in daily_calories.values():
    print(v)

print("all items......")
for k,v in daily_calories.items():
    print(k,v)

total_calories=daily_calories.get("tue",0)
print("tuesday calorie=",total_calories)

# add new key value total as total_consumed_calorie
total_calorie=0
for v in daily_calories.values():
    total_calorie+=v
print("total_calorie=",total_calorie)

#another method
daily_calories["total_calories"]=sum(daily_calories.values())
print(daily_calories)