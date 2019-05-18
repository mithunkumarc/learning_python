# Example number 2
from math import sqrt

# assertions

def test_example():
    '''test can contains callables(importing modules) with assertions'''
    print('running test example')
    assert sqrt(25) == 5






# A PyTest case will pass if:
#
#     It's assertions are True
#     (Or it doesn't have any assertions!)
#     And if it doesn't raise any unhandled Exceptions.




# command to run

# pytest -vs basic_test.py
# or
# pytest -q basic_test.py

# 1 passed test