"""
    *  5 row  4 space  1 column  => 6-row=1 
   **  4 row  3 space  2 column   =>6-4=2
  ***
 ****
*****
"""
def pattern():

    for r in range(5,0,-1):


        for s in range(1,r):

            print(" ",end="")

        for c in range(1,(6-r)+1):
          
          print("*",end="")

        print()    #next line

pattern()
