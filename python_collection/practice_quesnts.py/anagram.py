"""
 wirte a program to display anagrams

    words=["silent","listen","act","cat","note","tone","hen","chicken"]

    angarms=["silent","listen","act","cat","note","tone"]
"""

words=["silent","listen","act","cat","note","tone","hen","chicken"]
#index  0           1      2   3       4      5     6       7
#i      i
#j                  j

anagrams=set()   #duplicates not allowed in set
for i in range(0,len(words)):

    for j in range(0,len(words)):

        w1=words[i]
        w2=words[j]
        if sorted(w1)==sorted(w2) and w1!=w2:  #i and j not in same index
            anagrams.add(w1)
            anagrams.add(w2)
print(anagrams)
   