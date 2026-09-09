def inverted_half():

    for r in range(6,1,-1):

        for c in range(1,r):

            print(r-1,end="\t")

        print()

inverted_half()