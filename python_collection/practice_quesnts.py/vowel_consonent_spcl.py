text="hello$world#"
vowels=[]
consonent=[]
special=[]

for ch in text:
    if ch.lower() in "aeiou":
        vowels.append(ch)
    elif ch.isalpha():
        consonent.append(ch)
    else:
        special.append(ch)
print(vowels)
print(consonent)
print(special)