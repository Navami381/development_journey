placementcounts=[10,15,22,9,17,18]

feb_month_place=placementcounts[1]
print(feb_month_place)

placementcounts[0]=12
print("jan month placement count=",placementcounts[0])

print("filter count>15=======")
for count in placementcounts:

    if count>15:
        print(count)

print("highest placement count====")
max_count=placementcounts[0]
for  count in placementcounts:
    if count>max_count:
        max_count=count

print(max_count)

print("smallest placement count=======")
min_count=placementcounts[0]
for  count in placementcounts:
    if count<min_count:
        min_count=count

print(min_count)

print("second largest count=======")
first_max,second_max=0,0
for count in placementcounts:
    if count>first_max:
        second_max=first_max
        first_max=count
    elif count>second_max:
        second_max=count
print(second_max)






