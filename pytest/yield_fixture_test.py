# example 6
# yield allows us to do both pre-test and post-test actions,


import pytest


def test_with_yield_fixture(yield_fixture):
    print(f'running test with yield fixture : {yield_fixture}')
    assert 'foo' in yield_fixture




@pytest.fixture
def yield_fixture():
    '''
    fixtures can yield their data
    (additional code will run after that)
    '''

    print('PRE_TEST : initializing yield fixture')
    x = {'foo':'bar'}

    # remember , unlike generators , fixtures should only yield once(if at all)
    yield x

    #yield 100 no two yields are allowed in fixtures

    # this code runs after yield
    print('POST_TEST : cleaning up yield fixture')
    x = None


#  pytest -vs yield_fixture_test.py
# yield_fixture_test.py::test_with_yield_fixture PRE_TEST : initializing yield fixture
# running test with yield fixture : {'foo': 'bar'}
# PASSEDPOST_TEST : cleaning up yield fixture

