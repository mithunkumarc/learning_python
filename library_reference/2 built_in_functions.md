#### @classmethod : Transform a method into a class method. 

        ## example for @classmethod
        
        
#### compile() : Compile the source into a code or AST object. Code objects can be executed by exec() or eval().

                import ast
                codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
                file_name = 'sumstring'# optional
                #eval doest work for assingnment, os using exec
                codeObejct = compile(ast.parse(codeInString), filename = "" ,mode='exec')
                exec(codeObejct)
                eval(codeObejct)

                or
                
                codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
                codeObejct = compile(codeInString, filename = "" ,mode='exec')
                exec(codeObejct)
                eval(codeObejct)


#### complex() : Return a complex number with the value real + imag*1j or convert a string or number to a complex number. 
       
                
                print(complex(23,45))   # (23+45j)
                print(complex('23+8j')) # (23+8j)
                print(complex(45))      # (45+0j)
                # when it comes to sting , only one parameter is allowed
                # complex('23','8') # error
                
                
#### delattr() :  The delattr() deletes an attribute from the object (if the object allows it). works for "del attrname"

                class Person:
                    def __init__(self,id,name):
                        self.name = name
                        self.id = id

                p = Person(11,'rajat')
                delattr(p,'name')
                # del p.name
                print(p.id)
                print(p.name) # error : name property removed
     
     
#### dict() : Create a new dictionary. The dict object is the dictionary class.

        d = dict(name='vinay',id=100)
        print(d)    # {'name': 'vinay', 'id': 100}

        # using zip
        t = dict(zip([1,2,3],['a','b','c']))
        print(t)    # {1: 'a', 2: 'b', 3: 'c'}

        # list contains tuple as elements, each tuple contains key : value
        t = dict([(1,"one"),(2,True),(3,45.56)])
        print(t)    # {1: 'one', 2: True, 3: 45.56}


        t = dict([[1,"blue"],[2,'red'],[3,'yello']])
        print(t) # {1: 'blue', 2: 'red', 3: 'yello'}

        # creating dict
        e = dict({'three': 3, 'one': 1, 'two': 2})
                

#### dir() :  return a list of valid attributes for that object.

                class Person:
                    def __init__(self,name,id):
                        self.id = id
                        self.name = name

                print(dir(Person)) # properties available in Person class
                # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
                #  '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
                #  '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
                #  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
                #  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


                p = Person('kitty',40) # properties available in person object
                print(dir(p)) # along with dunder method , id and name also listed
                # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
                #  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
                #  '__init_subclass__', '__le__', '__lt__', '__module__',
                #  '__ne__', '__new__', '__reduce__', '__reduce_ex__',
                #  '__repr__', '__setattr__', '__sizeof__', '__str__',
                #  '__subclasshook__', '__weakref__', 'id', 'name']


                print(dir())  # attributes available in module
                # [ '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
                #  '__loader__', '__name__', '__package__', '__spec__']


#### divmod(a,b): returns quotient and remainder

                print(divmod(100,50))
                # output : (2,0) : (quotient, remainder)
                #Take two (non complex) numbers as arguments and return a pair of numbers
                # consisting of their quotient and remainder when using integer division
                
#### enumerate(iterable,start=0)

                returns a tuple containing a count (from start which defaults to 0) 
                and the values obtained from iterating over iterable.

                for i in enumerate(["csharp","java","python"]):
                    print(i)

                for i in enumerate(["csharp","java","python"],start=111):
                    print(i)

                 output : 
                        (0, 'csharp')
                        (1, 'java')
                        (2, 'python')
                        (111, 'csharp')
                        (112, 'java')
                        (113, 'python')
                        
                        
#### eval and exec : 

                        //covered 
                        

####  filter(function, iterable) : 
                        
                        //higer order function : covered
                        
                        
#### float() : Return a floating point number constructed from a number or string x.

                print(float("45.566"))
                ouput : 45.566


##### format(object,string) : Convert a value to a “formatted” representation, as controlled by format_spec. 
                        
                The interpretation of format_spec will depend on the type of the value argument.

                class Person:
                    def __init__(self,name,id):
                        self.name = name
                        self.id = id

                    def __format__(self, format_spec):
                        return f"id : {self.id} , name : {self.name} and address : {format_spec}"

                p = Person('rajat',43)
                print(format(p,"bangalore"))
                
                output : 
                id : 43 , name : rajat and address : bangalore


#### frozenset()  : immutable set

                s = {1,2,3}
                s.add(4)
                print(s)
                frozen_s = frozenset(s)
                print(frozen_s)         #       frozenset({1, 2, 3, 4})
                print(type(frozen_s))   #       <class 'frozenset'>
                
                # frozen_s.add(6) # error : cannot add new element : frozenset

#### 
