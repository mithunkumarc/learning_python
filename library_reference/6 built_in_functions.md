#### range() :  range is actually an immutable sequence type

              //covered
              
####  repr(object) : Return a string containing a printable representation of an object.

              // covered : __repr__() : magic method

#### reversed(sequence) : Return a reverse iterator. 


            # input : sequence
            # magic method : __reversed__()

            it = reversed([1,2,3,4,5])  # list is a sequence
            #it = reversed(range(1,6))  # range is a sequence
            #it = reversed((1,2,3,4,5))  # tuple is a sequence
            #it = reversed({1,2,3,4,5})# error : set object not reversible, set isnt sequence
            print(next(it))
            print(next(it))
            print(next(it))
            print(next(it))
            print(next(it))              


#### round() :  it returns the nearest integer to its input.

            print(34/6) # 5.6666666
            print(round(34/6)) # 6
            
#### set() : Return a new set object, optionally with elements taken from iterable. 

          #set(iterable)
          print(set({1,2,3,4,5})) 
          print(set((1,2,3,4,5))) # tuple to set
          print(set([1,2,3,4,5])) # list to set
          print(set({1:"one",2:"two",3:'Three'})) # set of keys
          
          
          
          
####  setattr(object, name, value): adding attribute to object. equivalent tot object.name = value
#### getatrr() : get value of attribute
            
              # setattr(object,name,value)
              class Mobile:
                  def __init__(self):
                      pass


              m = Mobile()
              setattr(m,"brand_name","motorola")
              #above line is equivalent to below line
              #m.brand_name = "motorola"
              print(m.brand_name)
              getattr(m,"brand_name","sony") # if there is no value then sony will be returned


#### slice(start, stop, step) : used to slice list, tuple, string
          
              #two ways to slice , list[start:stop:step] or list[slice(start,stop,step)]

              print(slice(10))    #slice(None,10,None)
              print(slice(1,10,5)) # slice(1,10,5)
              
              
              example : 
              l = [1,2,3,4,5,6,7,8,9,10,11,12]
              # with out slice , start : 2, end : 8, step : 2
              print(l[2:8:2])     # output : [3, 5, 7]

              # using slice(2,8,2)
              print(l[slice(2,8,2)]) # output : [3, 5, 7]

