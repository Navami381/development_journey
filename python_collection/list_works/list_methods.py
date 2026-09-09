colors=["red","green","blue","red","violet","purple"]
#          0    1       2      3       4        5
#add white color to colors
colors.append("white")      #add object at specified index
print(colors)

colors.insert(2,"orange")
print(colors)

colors.pop()
print(colors)

colors.remove("red")
print(colors)

blue_index=colors.index("blue")
print(blue_index)

red_count=colors.count("red")
print(red_count)

colors.reverse()
print(colors)

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

zara_fvt_food=["egg","chicken","tea"]
ayush_fvt_food=zara_fvt_food.copy()
ayush_fvt_food[0]="friedrice"
print("zara",zara_fvt_food)
print("ayush",ayush_fvt_food)