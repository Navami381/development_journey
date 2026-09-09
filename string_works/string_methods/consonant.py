word="pneumonoultramicroscopicilicovolcanoconisosis"
vowel_count=0
consonent_count=0
for ch in word:
 if ch.isalpha():
     if ch.lower() in "aeiou":
        
        vowel_count=vowel_count+1
     else:
        consonent_count+=1
    
    

print("vowel count=",vowel_count)
print("consonent count=",consonent_count)