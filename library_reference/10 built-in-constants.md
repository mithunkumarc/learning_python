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
            
            
            
