for r in range(1,8):

    for c in range(1,8):

        if r==1 or r==7  or c==1 or c==7 or c+r==8 or r==c:

            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()