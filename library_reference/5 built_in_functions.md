#### next : 

            # covered : __next__ : magic method
            
            
#### object() : returns an empty object. cannot add new properties/method

        You cannot add new properties or methods to this object.

        This object is the base for all classes, 
        it holds the built-in properties and methods which are default for all classes.


        x = object()
        print(x)
        print(type(x))
        print(x.__str__())
        # x.name = 'naumi' # error : cannot assing property/method to object
        # print(x.name)


        <object object at 0x7f332b579080>
        <class 'object'>
        <object object at 0x7f332b579080>
        

#### oct() : Convert an integer number to an octal string prefixed with “0o”.

          print(oct(8)) # 0o10
          print(oct(15)) # 0o17

          # ocatal possible literals : 0 to 7
          # at 8th postion we have 10
          # at 15th postion we have 17
          #octal :  0 1 2 3 4 5 6 7 10 11 12 13 14 15 16 17 20
          
#### open() : opens file for read and write

          list of mode of operation : 
          
          'r'       open for reading (default)
          'w'       open for writing, truncating the file first
          'x'       create a new file and open it for writing
          'a'       open for writing, appending to the end of the file if it exists
          'b'       binary mode
          't'       text mode (default)
          
#### ord(c) : return an integer representing the Unicode code point of that character.           

            inverse of chr()
            
            print(ord('a')) # 97
            print(ord('€')) # 8364


#### pow(x,y[,z]) :[x ** y % z] :  Return x to the power y; if z is present, return x to the power y, modulo z 

          (computed more efficiently than pow(x, y) % z). 
          The two-argument form pow(x, y) is equivalent to using the power operator: x**y.
          pow(x,y) : equivalent to x ** y
          
          
          print(10 ** 2 % 6)  # 100 % 6 is 4
          print(pow(10,2,6))  # same as above : output : 4
          print(pow(10,2))    # 100 : similar to 10 ** 2
          

#### print()

            #print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
            #need to pass flush=True otherwise output is buffered according to the sys.stdout buffer size.
            print(1,'hello',True,sep='=',end='\t',flush=True)
            # 1=hello=True	



#### property() : In Python, the main purpose of Property() function is to create property of a class. (similar to c# property)
#### better way to setter and getter
                        

              # Person class 
              class Person:
                  def __init__(self, name):
                      self._name = name

                  # getting the values
                  def getValue(self):
                      print('Getting name')
                      return self._name

                  # setting the values
                  def setValue(self, name):
                      print('Setting name ' + name)
                      self._name = name

                  # deleting the values
                  def delValue(self):
                      print('Deleting name')
                      del self._name

                  name = property(getValue, setValue, delValue, )


              # passing the value
              x = Person('rajat')
              print(x.name)       # get
              x.name = 'vijay'    # set
              del x.name          # del


              # Getting name
              # rajat
              # Setting name vijay
              # Deleting name


#### property using decorator : 

            #### Python program to explain property()
            #### function using decorator

            class Person:
                def __init__(self, name):
                    self._name = name

                # getting the values
                @property
                def name(self):
                    print('Getting name')
                    return self._name

                # setting the values
                @name.setter
                def name(self, name):
                    print('Setting value ' + name)
                    self._name = name

                # deleting the values
                @name.deleter
                def name(self):
                    print('Deleting name')
                    del self._name

                # name of all property functions are same as property


            x = Person('Peter')
            print(x.name)
            x.name = 'Diesel'
            del x.name

            output : 
            Getting name
            Peter
            Setting value Diesel
            Deleting name
