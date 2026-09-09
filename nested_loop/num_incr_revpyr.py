"""
1 2 3 4
1 2 3
1 2
1
"""
def inverted_half():

    for r in range(5,1,-1):

        for c in range(1,r):

            print(c,end="\t")

        print()

inverted_half()