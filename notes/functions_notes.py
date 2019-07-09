'''
    functions :
    A function is a block of code which only runs when it is called.
    You can pass data, known as parameters, into a function.
    A function can return data as a result.
'''

'''
    function with no input parameter and no return statement
'''
print('*'*20,'simple function with not input and return statement','*'*20)
def hello(): # no parameter defined
    print('hello world') # no return statment, just prints hello world on console


hello() # calling function hello()


'''
    function with input parameter and without return statement
'''
print('*'*20,'example for printing square of number','*'*20)
def square(number): # number : input parameter(variable declared in function)
    print(number * number)


square(5) # 5 : argument : value to be sent to parameter


'''
    function with input parameter and with return statement
'''
print('*'*20,'with input parameter and with return statement','*'*20)
def add(a,b): # a, b: input paramenters
    return a + b



result = add(10,20) # 10, 20 are arguments for function
print(result) # result : stores value returned by add(10,20) function call


'''
    function can call another function
'''
print('*'*20,'example : function calling another function','*'*20)
def helper():
    print('help main function')

def main():
    helper() # taking help from helper function


main()


'''
    default argument : parameter with default value/arguement
    default arguemnt must appear last in the parameter list
'''
print('*'*20,'example : default arguement','*'*20)
def greet(name,message='hello'): # message : parameter with default arguement
    # name : parameter without default value
    print(message,name)

greet('vijay') # vijay greeted with default value hello
greet('anil','welcome') # welcome replace default value hello for message


'''
    keyword argument : argument with key(name of parameter)
    keyword arugment must appear last in argument list
    positional arguemnt : argument without key(name of parameter)
    positional arugment must appear beginning in argument list
'''
print('*'*20,'example : keyword/positional arguemnt','*'*20)

def game(team1,team2='india'):
    print(team1,team2)

game('srilanka') # team1 : srilanka, team2 : india
game('sri lanka','australia') # team1 : srilanka, team2 : australia
game('sri lanka', team2='australia') # sri lanka : positional, australia : keyword argument
