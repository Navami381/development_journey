text="i have 2 car and 1 bike"
vowel_count=0
consonent_count=0
digit_count=0
for ch in text:
 if ch.isalpha():
     if ch.lower() in "aeiou":
        
        vowel_count=vowel_count+1
     elif ch.lower() not in "aeiou":
        consonent_count+=1
 elif ch.isdigit():
    digit_count=digit_count+1
    
    
    

print("vowel count=",vowel_count)
print("consonent count=",consonent_count)
print("digit count=",digit_count)

