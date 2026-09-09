"""
attendance = ["p","p","a","a","o","o","h"]

    write a program to print attendance count

"""
attendance = ["p","p","a","a","o","o","h"]
att_set=set(attendance)
att_count={}
for ch in att_set:
    att_count[ch]=attendance.count(ch)
print(att_count)
