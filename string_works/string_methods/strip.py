text="@hello@"

new_text=text.strip("@") #remove value from both end

print(new_text)

new_text1=text.lstrip("@") #remove value from beginning
print(new_text1)

new_text2=text.rstrip("@") #remove value from end
print(new_text2)