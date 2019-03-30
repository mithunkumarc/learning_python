#### among all attributes available on object some of them are readonly


        The implementation adds a few special read-only attributes to several object types, where they are relevant. 
        Some of these are not reported by the dir() built-in function.
        
        

#### object.__dict__ : A dictionary or other mapping object used to store an object’s (writable) attributes.
            
            # object.__dict__
            
            __dict__ is readonly, but it will list out properties(of object) which are writable
            
            
            print(object.__dict__.keys()) : 
            
                  dict_keys([
                  '__repr__', '__hash__', '__str__', '__getattribute__', 
                  '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', 
                  '__ne__', '__gt__', '__ge__', '__init__', '__new__', '__reduce_ex__', 
                  '__reduce__', '__subclasshook__', '__init_subclass__', 
                  '__format__', '__sizeof__', '__dir__', '__class__', '__doc__'
                  ])

            Example 2: 

            class Person:
                def __init__(self,name,age):
                    self.name = name
                    self.age = age

            p = Person('vinay',30)
            print(p.__dict__)
            
            ouput : {'name': 'vinay', 'age': 30}
            
####  instance.__class__: to which class it belongs to

            # instance.__class__
            
            class Person:
                def __init__(self,name,age):
                    self.name = name
                    self.age = age

            p = Person('vinay',30)
            print(p.__class__)
            # output : <class '__main__.Person'>


####  class.__bases__ : The tuple of base classes of a class object.

            # class.__bases__
            
            class Automobile:
                pass
            class Vehicle:
                pass

            class Truck(Vehicle,Automobile):
                pass

            print(Truck.__bases__)
            

#### definition.__name__ : The name of the class, function, method, descriptor, or generator instance.
                
            # definition.__name__    
        
            class Automobile:
                def move(self):
                    print("move")


            a = Automobile()
            print(Automobile.__name__) # Automobile : name of class
            print(a.move.__name__) # move : name of method
            print(__name__) # __main__ : module name in current context
            

####  definition.__qualname__

        definition.__qualname__:  
        The qualified name of the class, function, method, descriptor, or generator instance.

                class A:
                    class B:
                        class C:
                            def me(self):
                                print('__name__',type(self).__name__)           # output : __name__ : C
                                print('__qualname__',type(self).__qualname__)   # output : __qualname__ A.B.C


                demo = A.B.C()
                demo.me()



#### class.__mro__ : 

    class.__mro__
    
    This attribute is a tuple of classes that are considered when looking for base classes during method resolution.



                class A(object):
                    x = 10


                class B(A):
                    pass

                class C(A):
                    x = 15

                class D(B, C):
                    pass

                d = D()

                print(D.__mro__)
                
         output :       
         (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
