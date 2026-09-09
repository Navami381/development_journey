"""
ou are given two strings:

ransomNote - the note you want to create.
magazine - the letters available.

Determine whether you can construct the ransomNote using the letters from magazine.

Rules
You can use each letter from the magazine only once.
If a letter appears twice in the ransom note, it must appear at least twice in the magazine.
"""

def is_randsome(note,magazine):
      
 for char in note.lower():

    if char not in magazine.lower():

        print(False)

        break

 else:
    print(True)

is_randsome("Hen","chicken")
is_randsome("hens","chicken")