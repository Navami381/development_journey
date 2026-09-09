words=["madam","tan","ant","racecar","malayalam"]

palindrome_words=[]

for w in words:
   if w==w[::-1]:
    palindrome_words.append(w)
print(palindrome_words)