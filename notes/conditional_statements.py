'''
    conditional statements
    if , if else, else if, nested if

    switch statement not supported by python
    but it can be achieved using dictionary
'''

'''
    if : execute statements if condition is true
'''
print('*'*20,'if statement','*'*20)
print('*'*20,'example : check for even number','*'*20)
number = 100
if number % 2 == 0:
    print(number,'is even')



'''
    if else : else will execute when if statement fails
'''
print('*'*20,'if else statement','*'*20)
print('*'*20,'check for even or odd number','*'*20)
number = 101
if number % 2 ==0:
    print(number,'even')
else:
    print(number,'odd')


'''
    nested if : if can be declared inside another if statement
'''
print('*'*20,'nested if statement','*'*20)
print('*'*20,'check for even with positive or negetive','*'*20)
number = 100
if number % 2 == 0:
    if number > 0:
        print(number,'even and positive')
    else:
        print(number,'even and negetive')


'''
    elif : if you have more than two condtion to check use elif
'''
print('*'*20,'elif statement','*'*20)
print('*'*20,'example : largest among three numbers','*'*20)

a,b,c = 10,20,30
if a > b and a > c:
    print(a,'is largest')
elif b > a and b > c:
    print(b,'is largest')
else:
    print(c,'is largest')