words=["madam","aba","tan","sin","malayalam"]

fw=open("file_operation\\palindromes.txt","w")

for w in words:

    if w==w[::-1]:

      fw.write(w+"\n")