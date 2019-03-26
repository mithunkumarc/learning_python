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
                
                
                
