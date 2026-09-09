"""
A kangaroo word is a word that contains the letters of another word in the same order, but not necessarily next to each other.
"""


def is_kangaroo_word(source,target):
      
    if target in source:
        print(True)
    else:
        print(False)

is_kangaroo_word("kitchen","hit")
is_kangaroo_word("encourage","courage")
