"""
* * * * * *  6 row 0space 6 col  7-1=>6
 * * * * *   5 row 1space 5 col  7-2=>5
  * * * *
   * * *
    * *
     *

"""

for r in range(6,0,-1):

    for s in range(1,(6-r)+1):

        print(" ",end="")

    for c in range(1,r+1):

        print("*",end=" ")
        
    print()