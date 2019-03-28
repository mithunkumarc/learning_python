#### __debug__ : Remove assert statements and any code conditional on the value of __debug__.


          by default __debug__ is true
          assert and __debug__ are used to test code
          
          if you want assert statements and __debug__ in your program : 
          run script using : python3 <file_name.py>
          else using : python3 -O <file_name.py>
          
##### Example 1 : by default __debug__ is true ,which means we want assert statements
          
          filename : test.py
          
          print(__debug__) # True : by default value is True which supports assert statements
          assert(True) # no compalint
          assert(False) # you should see error : error indicates assert working
          
          #command : python3 test.py


##### Example 2 : running test.py using -O command which ignores or removes assert statements
          
          file name : test.py
          
          print(__debug__) # False : ignores assert statments
          assert(True) # will skip execution
          assert(False) # will skip execution
          
          ## command : python3 -O fun.py

          
          
          
          
