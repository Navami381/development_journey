text="a man is a canal panama"

consonent={ch for ch in text if ch not in "aeiou" and ch.isalpha()}
print(consonent)