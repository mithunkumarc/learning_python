'''
datatypes : defines the type of data and data comes in different forms.

    primitive datatypes : borrowed from c
    eg : int float string boolean

    builtin datatypes :  defined in python libraries
    eg : list, tuple, set ,dict, complex , None etc

    user defined datatypes: defined by user
    eg : Customer, Student, BankAccount etc

'''

'''
    1.primitive datatype
'''
print('*'*20,'primitive datatype','*'*20) # seperator line
'''
    int datatype
'''
number = 123
print('datatype of 123 ', type(number))

'''
    float datatype
'''
decimal_number = 77.89
print('datatype of 77.89 ',type(decimal_number))

'''
    both single and double quotes can be used to create strings
'''
word = 'hello world'
# word = "hello world"
print('data type of hello world',type(word))


'''
    boolean datatype
'''
flag = True
print('datatype of True is ',type(flag))
flag = False
print('datatype of False is ',type(flag))



'''
    2. builtin datatype 
'''
print('*'*20,'built in datatype','*'*20) # seperator line
print('builtin datatypes')
l = [1,2,3,4,5]
print('datatype of l is ',type(l))

t = (1,2,3,4,5)
print('datatype of t is ',type(t))

s = {'a','b','c','d','e'}
print('datatype of s is ',type(s))


c = 4+5j
print('datatpye of c is ',type(c))


'''
    None represents empty value. similar to null in c/java
'''
d = None
print('datatype of d is ',type(d))


'''
    3.user defined datatype
'''
print('*'*20,'user defined datatype','*'*20) # seperator line
class Customer:
    pass

c = Customer()
print('the datatype of c is ',type(c)) # <class '__main__.Customer'>

class Student:
    pass

s = Student()
print('the datatype of s is ',type(s)) # <class '__main__.Student'>