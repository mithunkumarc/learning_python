#### NotImplemented : used to indicate that the operation is not implemented with respect to the other type; 

          normally used with binary special method : (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) 
          Its truth value is true.


            class Player:
                def __init__(self,score):
                    self.score = score

                def __eq__(self, other):
                    if not isinstance(other,Player):
                        return NotImplemented
                    else:
                        return self.score == other.score

            class Computer:
                def __init__(self,score):
                    self.score = score

            p1 = Player(100)
            p2 = Player(100)
            p3 = Computer(300)
            print(p1.__eq__(p2)) # true : scores are equal and both type are Person
            print(p1.__eq__(p3)) # NotImplemented : cant compare other than player
            
            
            
#### truth value of NotImplemented is true


          print(bool(NotImplemented)) # True


#### Ellipsis : The same as the ellipsis literal “...”. 

          print(type(Ellipsis))   # <class 'ellipsis'>

          # literal value of ellipsis is ...
          print(type(...))        # <class 'ellipsis'>

          a = ...
          print(a) # Ellipsis



          # infinite data cant be displayed represented as ...
          # similar to reflection of glass opposite to each other
          a = [0]
          b = [0]
          a[0], b[0] = b, a   # a[0] -> b where b[0] -> a where a[0] -> b  ... soon
          print(a)
          print(b)

          # [[[...]]]
          # [[[...]]]

          # The variables a and b themselves aren't ' \
          # even "things" themselves, and they themselves are also merely pointers
          # to otherwise anonymous "things" in memory.

          # a -> [b] -> [[a]] -> [[[b]]] -> [[[[a]]]]
