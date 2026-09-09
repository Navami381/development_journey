"""
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
"""
for r in range(5, 0, -1):

    
    for s in range(1, r):
        print(" ", end="")

    
    for c in range(1, (6-r)+1):
        print(6-r, end=" ")

    print()