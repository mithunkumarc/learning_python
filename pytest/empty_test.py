# Example number 1
import pytest
# number of tests : 2
# only function which begins with test will get execute

def test_empty():
    '''by default function begins with test run by pytest'''
    pass

def empty_test():
    '''this test will not run by default because function does't begins with test'''
    pass


# pytest -q empty_test.py
# output : 1 passed