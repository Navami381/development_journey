"""
1
2 3
4 5 6
7 8 9 10
"""
def left_half():
    num=1

    for r in range(1,5):

        for c in range(1,r+1):

            print(num,end="\t")
            num=num+1

        print()

left_half()