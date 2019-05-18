# example 11
# a fixture receive parameters from another fixture , combines it and send it to test case
# output similar to last example, but the approach is different here
# also an example of skip test is also used

import pytest

@pytest.fixture(params=[1,2,3,4])
def numbers_fixture(request):
    '''
     Fixtures can cause tests to be run multiple times
     once per parameter
    '''
    yield request.param


@pytest.fixture(params=['a','b','c','d'])
def combine_fixture(request,numbers_fixture):
    '''
    fixtures can invoke each other
    producing cartesian products of params
    '''
    combined_param = request.param + str(numbers_fixture)
    yield combined_param
    # uncomment below lines to see fixture filtering
    if combined_param == 'b2':
        print('dont sink my batteleship')
        pytest.skip(combined_param + " : dont sink my batteleship ")



def test_advanced_fixtureception(combine_fixture):
    print(f'advanced fixture param combine : {combine_fixture} ')