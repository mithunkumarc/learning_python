'''
    arrays : import array module

    typecode :  The typecode character used to create the array.

    i : int
    l : long
    s : short
    f : float
    d : double
    u : unicode character

    syntax :   import array
               variable = array.array(typecode,[elem1,elem2,..]

    itemsize : The length in bytes of one array item in the internal representation.

    append(x) : Append a new item with value x to the end of the array.


    count(x) : Return the number of occurrences of x in the array.

    extend(iterable) : Append items from iterable to the end of the array.

    len(array) : size of array

    index(x) : Return index of the first occurrence of x in the array.



    insert(position,x) : Insert a new item with value x in the array before position i

    pop(i) : Removes the item with the index i from the array and returns it.

    remove(x) :     Remove the first occurrence of x from the array.

    reverse() :      Reverse the order of the items in the array.

    tolist() : Convert the array to an ordinary list with the same items.



'''

import array
numbers = array.array('i',[1,2,3,4,5])
print('datatype of numbers ',type(numbers))
numbers.append(6) # adding new element 6 to numbers
print('after adding element 6 to numbers : ',numbers)
print('memory size of each item :integers : ',numbers.itemsize) # output : 4
print('total number of elements in array : ',len(numbers))
print('-'*50) # seperator


'''
    string array is not allowed, only char is allowed
'''
words = array.array('u',['h','e','l','l','o'])
# words = array.array('u',['hello'])
print('character array : ',words)
print('memory size of each character : ',words.itemsize) # output : 4
print('-'*50) # seperator



'''
    creating boolean array
'''
flags = array.array('b',[True,True,False,False])
print('memory size of each boolean item : ',flags.itemsize) # output  :1
print('-'*50) # seperator


'''
    creating float array
'''
decimals = array.array('f',[4.4,5.5,6.6])
print('memory size of each float item : ',decimals.itemsize)
print('-'*50) # seperator


''' 
        count(x) : Return the number of occurrences of x in the array.

'''
data = array.array('i',[100,200,300,400,200,200])
print('total number of apperance of element 200 : ',data.count(200)) # output : 3
print('-'*50) # seperator



'''
    extend(iterable) : Append items from iterable to the end of the array.
'''
data = array.array('i',[10,20,30,40,50])
new_data = array.array('i',[60,70,80,90,100])
data.extend(new_data)
print('after adding new data 60 to 100 : ',data)
print('-'*50) # seperator




'''
    index(x) : Return index of the first occurrence of x in the array.
'''
data = array.array('u',['a','e','i','o','u'])
print('index position of letter "i" is : ',data.index('i')) # output : 2
print('-'*50) # seperator





'''
    insert(position,x) : Insert a new item with value x in the array before position i
'''
data = array.array('f',[1.1,3.3,4.4,5.5])
data.insert(1,2.2)
print('2.2 inserted at index 1 :',data)
print('-'*50) # seperator




'''
    pop(i) : Removes the item with the index i from the array and returns it.
'''
data = array.array('i',[11,22,33,44,55])
print('element removed from position 2 is : ',data.pop(2))
print('after removing 33 , data is : ',data)
print('-'*50) # seperator



'''
 remove(x) :     Remove the first occurrence of x from the array.
'''
data = array.array('i',[21,22,23,24,25])
data.remove(23)
print('deleting 23 using remove method ',data)
print('-'*50) # seperator



'''
    del operator
'''
data = array.array('i',[21,22,23,24,25])
data.remove(23)
print('deleting 23 using delete operator ',data)
print('-'*50) # seperator




'''
    reverse() :      Reverse the order of the items in the array.
'''
data = array.array('u',['n','i','n','e'])
data.reverse()
print('after reverse method : ',data)
print('-'*50) # seperator



'''
        tolist() : Convert the array to an ordinary list with the same items.
'''
data = array.array('u',['n','i','n','e'])
char_list = data.tolist()
print('after array to list conversion : ',char_list)
print('check the datatype : ',type(char_list))
print('-'*50) # seperator


