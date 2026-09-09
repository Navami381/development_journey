"""
word="python programming is simple"
    write a program to print character count
"""
word="python programming is simple"
word_set=set(word)
char_count={}

for ch in word_set:
    char_count[ch]=word.count(ch)
    
print(char_count)