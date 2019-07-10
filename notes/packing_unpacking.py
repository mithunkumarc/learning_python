''' packing unpacking arguments '''

'''
    packing : 
    When we don’t know how many arguments need to be passed to a python function, 
    we can use Packing to pack all arguments in a tuple/dictionary.
    
    * : used to pack arguments into tuple
    ** : used to pack arugemnts into dictionary
'''

'''
    why packaging : 
    consider below function, it works for fixed number of parameters
    it will not work for different number of arguments
'''
print('*'*20,'without packing','*',20)
def find_avg(a,b,c):
    # ignore logic
    total = a + b + c
    avg = total/3
    return avg

print(find_avg(10,20,30))
# find_avg(10,20) # error
# find_avg(10,20,30,40) # error


'''
    with packing: multiple arguments are packed as tuple
    * : used to pack as tuple
'''
print('*'*20,'with packing, exampe : tuple','*'*20)
def average(*data): # type(data) : tuple, * indicates tuple
    total = sum(data)
    result = total/len(data)
    return result

print('avg of three arguments : ',average(10,20,30)) # arguments 10,20,30 packed as tuple
print('avg of four arguments : ',average(10,20,30,40))
print('avg of two arguments : ',average(10,20))


'''
    keyword arguments are packed as dictionary
    ** : used to pack as dictionary
'''
print('*'*20,'packing as dictionary','*'*20)
def league_matches(**matches): # **matches : packed as dictionary
    for match in matches:
        print(match,matches[match])



league_matches(m1 = 'ind vs aus', m2 = 'sri vs nz', m3 = 'eng vs sa')


'''
    unpacking example
    list , tuple and set can be unpacked 
    set : not predictable
'''

'''
    unpacking list
'''
print('*'*20,'unpacking list','*'*20)
a,b,c = [10,20,30]
print('unpacking list : ',a,b,c)
a,*b,c = ['one','two','three','four','five']
# *a,b,c = ['one','two','three','four','five'] # try this
# a,b,*c = ['one','two','three','four','five'] # this this too
print('unpacking and packing together : ',a,b,c)




'''
    unpacking tuple
'''
print('*'*20,'unpacking tuple','*'*20)
def square_cube(number):
    return (number * number , number * number * number) # returning tuple

square_result , cube_result = square_cube(3) # tuple got unpacked to two variables
print(square_result)
print(cube_result)



'''
    unpacking set
    run multiple time to see inconsistant result
'''
print('*'*20,'unpacking set','*'*20)
a,b,c = {'hello',234,True}
print('unpacking set : ',a,b,c)