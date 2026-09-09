"""
Check if a character is a vowel or consonant.
"""

ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")