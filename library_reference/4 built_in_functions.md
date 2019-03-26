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
                  
                  
