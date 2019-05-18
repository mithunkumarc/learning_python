# example 9 :
# params used to send input to test functions
# instead of creating seperate test cases for each test data
# use params to use same test case for mutiple input



import pytest
def test_parameterization(letter):
    print(f'running test_parameterization {letter}')

def test_modes(mode):
    print(f'running test modes with {mode}')


# 5 test case data with out label for each test
@pytest.fixture(params=['a','e','i','o','u'])
def letter(request):
    '''
    Fixtures with parameters will run once per param
    you can access the current param via the request fixture
    '''
    yield request.param



# output : params_test.py::test_parameterization[a] running test_parameterization a
# .... same for rest of the input


# ids are used as label for each test
# three test cases with label(ids) for each test
@pytest.fixture(params=[1,2,3],ids = ['foo','bar','baz'])
def mode(request):
    '''
    Fixtures with parameters will run once per param
    you can access the current param via the reques fixture
    '''

    yield request.param



# params_test.py::test_modes[foo] running test modes with 1
# PASSED
# params_test.py::test_modes[bar] running test modes with 2
# PASSED
# params_test.py::test_modes[baz] running test modes with 3
# PASSED



# command : pytest -vs params_test.py