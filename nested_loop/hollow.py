"""
     *       Row 1 → 5 spaces                            
    * *      Row 2 → 4 spaces 
   *   *     Row 3 → 3 spaces
  *     *    
 *       *   
* * * * * *  

"""
for r in range(1,6):

    for c in range(1,10):

        if r+c==6 or c-r==4 or r==5:

            print("*",end="")

        else:

            print(" ",end="")
            
    print()