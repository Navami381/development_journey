# def is_palindrome(word):

#     reverse = "" 

#     for ch in word:
#         reverse = ch + reverse

#     if word == reverse:
#         print("Palindrome")
#     else:
#         print("Not a Palindrome")


# is_palindrome("madam")
# is_palindrome("hello")

def is_palindrome(word):
    if word==word[::-1]:
        print(True)
    else:
        print(False)

is_palindrome("madam")
is_palindrome("racecar")
is_palindrome("cat")