# example 7
# pytest -vs request_fixture.py


import pytest

# request can be used to instrospect or know the context of text case
# used to know about testcase name , module name and scope

def test_with_introspection(introspective_fixture):
    print('running test with introspection')
    assert True


@pytest.fixture
def introspective_fixture(request):
    '''
    The request fixture allows introspection into the
    requesting test case
    '''
    print('introspective fixture')
    print(f'called at {request.scope}') # function scope
    print(f'in the module {request.module}') # current module name where test running
    print(f'on the {request.node} node') # node name same as test case name : test_with_introspection

