#### getattr(object, name[, default])

        //convered
        
#### globals() : Return a dictionary representing the current global symbol table.(module info)

          # using globals() , we can add global level properties/attributes/variable
          def global_test():
              a = 1
              b = 2
              huh = globals()
              c = 3
              print(huh)
              huh['d'] = 4    # creating attribute or variable d in global scope
              print(huh)

          global_test()
          print(d) # 4
        
          output  :
          {'__name__': '__main__', '__doc__': None, '__package__': None, 
          '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fb234c5f0b8>, 
          '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 
          '__file__': '/home/mitun/PycharmProjects/tad/testdatastructures.py', '__cached__': None, 
          'global_test': <function global_test at 0x7fb234c83e18>, 'd': 4}
          4

  

#### locals() ; local scope state. returns list of local variables.

          def local_test():
              a = 1
              b = 2
              huh = locals()
              c = 3
              print(huh)
              huh['d'] = 4
              print(huh)

          local_test()
          # print(d) # d not accessible outside local_test()
          
          output : 
          
          {'b': 2, 'a': 1}
          {'b': 2, 'a': 1, 'd': 4}


####  hasattr() :  The result is True if the string is the name of one of the object’s attributes, False if not.

          p = "hello"
          print(hasattr(p,"format"))

          class Person:
              name = "hello"

          print(hasattr(Person(),"name"))
          
          
          
#### hash()  : also id() vs hash()

          # id() vs hash()

          # id() : all objects can have id() , returns memory location of object


          # hash value must not change, because it being used as index
          # hash value depends on the content of object
          # if there is a change in content thay may affect hashvalue
          # so only immutalbe objects can have hashvalue
          # immutalbe objects can be called as hashable objects
          
          l = (1,2,3)
          print(id(l))
          print(hash(l))


        # output : may vary
        
        140257266044288
        2528502973977326415
        
        
        
#### help() : opens interactive session to list modules, keywords ,symbols etc

        help()
        
        # execute 
        opens : 
        help> keywords   <- enter
        
        
        
