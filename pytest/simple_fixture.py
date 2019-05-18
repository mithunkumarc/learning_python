# example 4 :
# same role as setup and teardown method of unittest.TestCase

import pytest

def test_with_local_fixture(local_fixture): # local_fixture define later this code
    '''
    fixtures can be invoked simply by having a positional arg
    with the same name as fixture
    '''
    print('running test_with_local_fixture')
    assert True


# local fixture : local to module
@pytest.fixture
def local_fixture():
    '''fixtures are callables(functions) decoratred with @fixture'''
    print('doing local fixture setup stuff')

# globla fixture : other module can access
@pytest.fixture(scope='module') # important
def global_fixture():
    '''fixtures are callables(functions) decoratred with @fixture'''
    print('doing global fixture setup stuff')


########################
# in another file , to use global_fixture

# import pytest
# from simple_fixture import global_fixture
# def test_with_global_fixture1(global_fixture): # local_fixture define later this code
#     print('running test_with_global_fixture')
#     assert True

########################