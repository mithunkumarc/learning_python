#### Returns a new tuple subclass named typename.

        The new subclass is used to create tuple-like objects that have
        fields accessible by attribute lookup as well as being indexable and iterable.


          from collections import namedtuple
          person = namedtuple('person','first_name last_name')
          print(type(person)) # subclass of tuple
          p = person('joe','schmoe') 
          print(p.first_name)  # joe

          P = namedtuple('Point',['x','y'])
          pt = P(11, y = 12)
          print(pt[0])
          print(pt.y)


          print(pt.count(11)) # appear 1 time
          print(pt.index(12))# 1 , index of 12
