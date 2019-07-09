'''
    lambda function
    A lambda function is a small anonymous function.
    A lambda function can take any number of arguments, but can only have one expression.
'''

'''
    function with name
'''
print('*'*20,'example : function with name','*'*20)
def add(a,b):
    return a + b

print(add(3,4))


'''
    lambda function for addition of two numbers
'''
print('*'*20,'example : lambda for addition','*'*20)
add = lambda a,b : a + b # a, b :input parameter, a+b: output value
result = add(13,6)
print(result)

'''
    examples : lambda
'''
difference = lambda a,b : a - b
multiply = lambda a,b : a * b
division = lambda a,b : a / b


'''
    lambda can be self called
    function calling itself
'''
print('*'*20,'example : self calling lambda','*'*20)
result = (lambda a : a * a)(5)
print(result)


'''
    lambda function can be passed as value
'''
print('*'*20,'example : lambda as value to another function','*'*20)
def recipe(prepare_food):
    prepare_food()

# below lambda has no input parameter
prepare_food_logic = lambda : print('prepare food implemenation')

recipe(prepare_food_logic)



