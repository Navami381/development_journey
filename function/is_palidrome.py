def is_palindrome(word):

    reverse = "" 

    for ch in word:
        reverse = ch + reverse

    if word == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")


is_palindrome("madam")
is_palindrome("hello")