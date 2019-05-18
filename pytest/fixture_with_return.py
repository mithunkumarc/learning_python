# example 5
# in last example , fixture was just printing message
# in this example , fixture will return value
import pytest

def test_with_data_fixture(one_fixture):
    '''
    pytest finds the fixture whose name matches the arguemnt,
    calls it, and passes that return value into our test case:
    '''
    print(f'value is : {one_fixture}')


@pytest.fixture
def one_fixture():
    '''
    Beyond just doint stuff, fixtures can return data
    which pytest will pass to the test cases that refer to it...
    '''
    print('returning 1 from data_fixture')
    return 1


# to read output use command
# pytest -vs fixture_with_return.py
