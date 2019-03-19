#### abs() : returns the absolute value(unsigned) of number.

            # argument may be integer or float or complex number
            # in case of complex number , magnitude is returned

            print(abs(12))          # 12
            print(abs(-12))         # 12
            print(abs(12.34))       # 12.34
            print(abs(-12.34))      # 12.34
            print(abs(-12+4j))      # 12.64
            print(abs(12-4j))       # 12.64
            
#### all(iterable) : returns true if all are true. or iterable is empty 

            print(all([True,True,True]))        # True : all are true
            print(all([False,False,False]))     # False : all are false
            print(all([True,False,True]))       #False : one of them is false
            print(all([1,1,1]))                 # True : all are 1
            print(all([0,0,0]))                 # False : all are 0
            print(all([1,0,1]))                 # False : one of the is 0
            print(all([]))                      # True : empty



#### ascii() : prints string representation of ascii but skips non ascii characters


            print("is")# output : is : i and s are ascii characters
            print(ascii("ö is"))# '\xf6 is' : ö is a non ascii and skipped
            print(ascii("√ is"))# '\u221a is' 


#### bin(number) : return binary format : return type string. prefixed with 0b

            print(bin(23)) # 0b10111
            print(bin(-34)) # -0b100010
            
            
            
