def pyramidPattern(rows): 
	for row in range(1, rows):
	    num = 1
	    for j in range(rows, 0, -1):
	        if j > row:
	            print(" ", end='')
	        else:
	            print("$", end='')
	            num += 1
	    print("=",end="")
	    for j in range(rows):
	    	if j < row:
	    		print("$",end="")
	    print("")

# send number of rows
pyramidPattern(10)	    


'''
sample output : 
         $=$
        $$=$$
       $$$=$$$
      $$$$=$$$$
     $$$$$=$$$$$
    $$$$$$=$$$$$$
   $$$$$$$=$$$$$$$
  $$$$$$$$=$$$$$$$$
 $$$$$$$$$=$$$$$$$$$
'''
