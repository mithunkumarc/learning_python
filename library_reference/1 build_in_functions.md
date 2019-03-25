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
            

#### bool() : 

            print(bool(True)) # True
            print(bool(False))  # False

            # bool() : returns zero for false , non zero returns true
            print(bool(0))  # False
            print(bool(1))  # True
            print(bool(123)) # True
            print(bool(-1)) # True
            print(bool(-12)) # True

            # bool() : string
            print(bool(""))     # empty string : false
            print(bool("True")) # Non empty string : true
            print(bool("False")) # Non empty string : true
            print(bool("hello")) # Non empty string : true

            # bool(None)
            print(bool(None))  # False


#### breakpoint : tobe updated : added in 3.7


            //example
            
            
#### bytearray : array of bytes

            string = "zen of python."
            # string with encoding 'utf-8'
            arr = bytearray(string, 'utf-8')
            print(arr)              #   bytearray(b'zen of python.')
            print(type(arr))        #   <class 'bytearray'>


#### bytes : 
            
            # using utf-8 encoding
            sentence = "zen of python."
            byteString = bytes(sentence,'utf-8')
            print(byteString)
            print(type(byteString))

            # using byte string
            sentence = b'zen of python' #byte string
            bytesString = bytes(sentence)
            print(byteString)
            print(type(byteString))


#### bytes vs bytearray


                bytes objects are immutable sequences of single bytes

                bytearray objects are a mutable counterpart to bytes objects.

            

#### callable  : returns true if object is callable
            
            # callable ojbect : implemented dunder method __call__()
            # allows us to operate on object same way as function
            # object can be used as function

            class Person():
              pass

            print(callable(Person())) # False

            class Employee():
              def __call__(self, *args, **kwargs):
                  print("i am callable")

            print(callable(Employee())) # True
            


#### chr() :  Return the string representing a character whose Unicode code point is the integer i.

            print(chr(97)) # a
            print(chr(98)) # b
            print(chr(1_114_111))
            # char rangle : 1 to 1_114_111
            # a
            # value error outside 1_114_111
            # print(chr(1_114_112)) # error

