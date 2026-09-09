"""
slicing is ectracting a portion from sequence
"""

text="A man, a plan, a canal panama"
#     01234567890123456789012345678
#               1         2
substr=text[17:22]
print(substr)

substr=text[9:13]
print(substr)

substr=text[23:]
print(substr)

substr=text[:5]
print(substr)

copy_str=text[:]
print(copy_str)