#### hex() : converts to hexadecimal

      print(hex(123))
      #0x7b
      
#### id() : Return the “identity” of an object. (mem location)


      This is an integer which is guaranteed to be unique and constant for this object during its lifetime      
      CPython implementation detail: This is the address of the object in memory.


        print(id([1,2,3]))
        #output : 140697967597000    
        

#### input([prompt]) : reads input as string from console.

        t = input("enter a word")
        print(t)
        
#### int() : converts string form to int

        print(int())     # ouput  : 0
        print(int("12")) # output : 12
        # print(int("hello")) # invalid literal : ValueError
        
        
#### isinstance : checks object belongs to specific type        

          word = "python"
          print(isinstance(word,str)) # true

          class Person:
              pass
          p = Person()
          print(isinstance(p,Person)) # true
          
          
#### issubclass : checks whether a class is subclass of specific type

          class Person:
              pass

          class Doctor(Person):
              pass

          print(issubclass(Doctor,Person)) # true
          
          
#### iter() : Return an iterator object. 


#### len() : Return the length (the number of items) of an object.


#### list() : converts string letters,tuple,set,dict keys to list

            print(list("hello")) # list of letters
            print(list([1,2,3])) # list 
            print(list({1:"name",2:"age"})) # list of dict keys [1,2]
            print(list({1,2,3})) # set to list
            
            
#### map(function,iterable) : higer oder function

            covered
            
#### max(*args,key=function) : 

                  print(max([1,2,3])) # output : 3
                  
                  #print(max([1,2,3,"hello"])) # not supported between int and string
                  print(max({1,2,3})) #  output : 3
                  print(max({1:"name",2:"age",3:"address"})) # maximum index, output 3
                  print(max(1,2,3)) # tuple : output 3

                  class Person:
                      def __init__(self,id):
                          self.id = id

                  p1 = Person(11)
                  p2 = Person(22)
                  p3 = Person(33)
                  max_id_person = max(p1,p2,p3,key=lambda x : x.id)
                  print(max_id_person.id) # output : 33
                  
                  
#### memoryview : Return a “memory view” object created from the given argument.  :incomplete

            memoryview objects allow Python code to access the internal data of an object 
            that supports the buffer protocol without copying.
            
            # object(data) stored as bytes in memory
            # memoryview allows us to view internal data of object(memory)
            # memoryview : the condition is object must have been stored as bytes


            A memoryview supports slicing and indexing to expose its data. 
            One-dimensional slicing will result in a subview:

            v = memoryview(b'abcefg')           # memoryview : supports only byte form of data
            print(v[1])             #98(viewing first element)
            print(v[-1])            #103
            print(v[1:4])           #<memory at 0x7f3ddc9f4350>
            print(bytes(v[1:4]))    #b'bce' (reading in original form)


            rList = [1, 2, 3, 4, 5]
            arr = bytearray(rList)  # converting to bytes
            # now arr is eligible for memoryview            
            mem_view = memoryview(arr)
            print(mem_view.tolist())      # [1, 2, 3, 4, 5] : original form
            print(mem_view.tobytes())     # b'\x01\x02\x03\x04\x05'
            # object to bytes example is needed
            
            
            
            ### note : object to byte : example needed
            
            
#### min : 

            print(min(3,4,5))       #   3
            print(min(12,34,5,6))   #   5
            print(min('hello world','hi python','hai',key= len))    #   hai
            print(max('hello world','hi python','hai',key= len))    #   hello world

            # example 2 : with iterable
            def divide(number):
                return number/2

            num = [15, 300, 2700, 821, 52, 10, 6]
            print('Minimum is:', min(num, key=divide)) #Minimum is: 6

