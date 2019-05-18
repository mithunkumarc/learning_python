# example 14

# parameter without fixture

import pytest

@pytest.mark.parametrize("number",[1,2,3,4,5])
def test_numbers(number):
    '''
    mark can be used to play inline parametrization , without a fixture
    '''
    print(f'running test numbers with : {number}')


@pytest.mark.parametrize("x,y",[(1,'a'),(2,'b'),(3,'c')])
def test_dimenstions(x,y):
    '''
    mark.parametrize can even unpack tuples into named parameters
    '''
    print(f'running test with x : {x}, y : {y}')



# test case with label for each test data
@pytest.mark.parametrize("mode",[1,2,3],ids=['foo','bar','baz'])
def test_modes(mode):
    '''
    the ids kwarg can be used to rename paramerts
    '''
    print(f'running test modes with : {mode}')


