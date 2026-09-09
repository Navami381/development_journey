text="the quick brown fox jumps over lazy dog"

alphabets="abcdefghijklmnopqrstuvwxyz"

for alpha in alphabets:

    if alpha not in text:
        print("not a pangram")
        break
else:
    print("pangram")