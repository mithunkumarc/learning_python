#### @staticmethod : Transform a method into a static method.

            class Student:
                @staticmethod
                def get_course():
                    return "science"

            print(Student.get_course()) # science 
    
    
#### str() : Return a str version of object. See str() for details.

            print(str(1), type(str(1)))
            print(str(True), type(str(True)))
            print(str([1,2,3]),type(str([1,2,3])))
            print(str(34.45),type(str(34.45)))
            # output : 
            # 1 <class 'str'>
            # True <class 'str'>
            # [1, 2, 3] <class 'str'>
            # 34.45 <class 'str'>


#### sum()  :  returns the total. start defaults to 0. 

            print(sum([1,2,3,4,5]))                 # 15
            # print(sum([1,2,3,4,[1,2,3]]))         # error : embedded list
            print(sum({200,300,400}))               # 900
            print(sum({1:"one",2:"two",3:"three"})) # sum of keys
            

#### super() :(super in java)  The super() builtin returns a proxy object that allows you to refer parent class by 'super'.


            class Mobile:
                def phone_call(self):
                    print("mobile phone call")

            class Samsung(Mobile):
                def phone_call(self):
                    super().phone_call() # calling base class phone_call()

            s = Samsung()
            s.phone_call()
            
            
            
            ouptut : mobile phone call


#### tuple() : list,set,dict keys,range to tuple


              print(tuple([1,2,3,4,5]))  # list to tuple
              print(tuple({1,2,3,4,5}))  # set to tuple
              print(tuple({1:"one",2:"two",3:"three"})) # dict keys to tuple
              print(tuple(range(1,11))) # range to tuple

              # ouput : 
              # (1, 2, 3, 4, 5)
              # (1, 2, 3, 4, 5)
              # (1, 2, 3)
              # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
              

#### type(value) : 

                print(type(123))
                print(type("hello"))
                print(type(56.66))
                print(type([1,2,3])) # list
                print(type({})) # dict
                print(type(set({}))) # set
                print(type(NotImplemented))


                class Employee:
                    pass

                print(type(Employee()))
                # games
                # <class 'int'>
                # <class 'str'>
                # <class 'float'>
                # <class 'list'>
                # <class 'dict'>
                # <class 'set'>
                # <class '__main__.Employee'>
                # <class 'NotImplementedType'>


#### vars() : displays module attributes with variables in dict form

            # Return the __dict__ attribute for a module, class,
            # instance, or any other object with a __dict__ attribute.

            count = 100
            color = "black"
            print(vars())


            def add(a,b):
                return a+b

            add(3,4)

            # {'__name__': '__main__', '__doc__': None, '__package__': None,
            #  '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fd8adf1f128>,
            # '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
            # '__file__': '/home/mitun/PycharmProjects/tad/fun.py', '__cached__': None,
            # 'count': 100, 'color': 'black'}



####  zip(*iterables) :  Make an iterator that aggregates elements from each of the iterables. : output : tuple of zipped elements

              for i in zip([1,2,3]):
                  print(i)

              # (1,)
              # (2,)
              # (3,)

              for i in zip([1,2,3],("one","two","three")):
                  print(i)

              # (1, 'one')
              # (2, 'two')
              # (3, 'three')

              #make sure set has unique elements or else u lose one iteration
              
              for i in zip([1,2,3],("one","two","three"),{"click","hover","scroll"}):
                  print(i)

              # (1, 'one', 'click')
              # (2, 'two', 'scroll')
              # (3, 'three', 'hover')


#### __import__() :  is an advanced function that is called by the import statement.
            
            # This __import__() function is not necessary in everyday Python programming. 
            # It is rarely used and often discouraged.
            mathematics = __import__('math')
            
            
            print(mathematics.fabs(-2.5)) # absolute(magnitude) value of float number :
            # output : 2.5
