words=["hello","hai","hello","wow","silent","active","hello"]

word_count={w:words.count(w) for w in set(words)}
print(word_count)