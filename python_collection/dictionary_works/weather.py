oneweek_weather={"sun":33.5,"mon":22.2,"tue":33.2,"wed":20,"thur":10.3,"fri":40.6,"sat":80.6}
print(oneweek_weather)

sat_weather=oneweek_weather["sat"]
print("saturday weather=",sat_weather)

oneweek_weather["wed"]=30.9
print(oneweek_weather)