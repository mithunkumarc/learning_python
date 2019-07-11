'''shallow and deep copy'''

'''
    shallow copy : content(same memory location) shared across two object
    
'''
original_copy = [[1,2,3],['a','b','c'],[True,False]]

import copy
shallow_copy = copy.copy(original_copy) # creating shallow copy
print('shallow copy : ',shallow_copy)
print('memory location of first element of original copy : ',id(original_copy[0]))
print('memory location of first element of shallow copy : ',id(shallow_copy[0]))


'''
    deep copy : new copy of content will be created across two objects
'''
deep_copy = copy.deepcopy(original_copy)
print('deep copy : ',deep_copy)
print('memory location of first element of deep copy : ',id(deep_copy[0]))