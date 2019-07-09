'''
    looping statements : executes code multiple times

    for and while loop

    do while loop not defined in python
'''
'''
    for : when starting and ending iteration is known
    for loop also used to read datastructures and sequences
'''

for i in range(1,10,1): # generate numbers from 1 to 9 with step 1
    print(i)
else:
    print('end of for loop')



'''
    while : when starting and ending iteration is unknown
    while loop executes statements as long as condition is true
'''
number = 50
while number < 100:
    print(number)
    number = number + 1
else:
    print('end of while loop')