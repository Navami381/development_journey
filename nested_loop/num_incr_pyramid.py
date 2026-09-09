"""
1
1 2
1 2 3 
1 2 3 4
"""
def left_half():

    for r in range(1,5):

        for c in range(1,r+1):

            print(c,end="\t")

        print()

left_half()