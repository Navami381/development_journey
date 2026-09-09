"""
A pangram is a sentence that contains every letter of the English alphabet (A to Z) at least once.

There are 26 letters in the English alphabet, and a pangram must include all of them.
"""
def is_pangram(word):
 
 alphabets="abcdefghijklmnopqrstuvwxyz"

 for ch in alphabets:

    if ch not in word.lower():     
        print(False)
        break
 else:
    print(True)

is_pangram("The quick brown fox jumps over lAzy dog")

is_pangram("the quick brown fox jumps over lay dog")
    