#### wrapper around dictionary objects for easier dict subclassing
#### example for joining two dict

        from collections import UserDict
        class FancyDict(UserDict):
            def __init__(self,data={},**kw):
                UserDict.__init__(self)
                self.update(data)
                self.update(kw)

            def __add__(self, other):
                new_dict = FancyDict(self.data) # a
                new_dict.update(other) # b
                return new_dict

        a = FancyDict(a = 1) # goes to kw
        b = FancyDict(b = 2)
        print(a + b)

        # output : 
        # {'a': 1, 'b': 2}
