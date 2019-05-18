# example 10
# to generate all possible combinations and permutations of a set of data
# two fixtures combining params

import pytest

def test_fixturecetion(letters_fixture, numbers_fixture):
    '''
    printout our combined fixture product
    '''
    combined_data = letters_fixture + str(numbers_fixture)
    print(f'running combined fixture data : {combined_data}')


@pytest.fixture(params=['a','b','c','d'])
def letters_fixture(request):
    '''
    fixtures can cause tests to be run multiple times
    once per parameter
    '''
    yield request.param


@pytest.fixture(params=[1,2,3,4])
def numbers_fixture(request):
    '''
    fixtures can invoke each other
    producing cartesian products of parameters
    '''
    yield request.param


# pytest -vs params_combination.py



# params_combination.py::test_fixturecetion[a-1] running combined fixture data : a1
# PASSED
# params_combination.py::test_fixturecetion[a-2] running combined fixture data : a2
# PASSED
# params_combination.py::test_fixturecetion[a-3] running combined fixture data : a3
# PASSED
# params_combination.py::test_fixturecetion[a-4] running combined fixture data : a4
# PASSED
# params_combination.py::test_fixturecetion[b-1] running combined fixture data : b1
# PASSED
# params_combination.py::test_fixturecetion[b-2] running combined fixture data : b2
# PASSED
# params_combination.py::test_fixturecetion[b-3] running combined fixture data : b3
# PASSED
# params_combination.py::test_fixturecetion[b-4] running combined fixture data : b4
# PASSED
# params_combination.py::test_fixturecetion[c-1] running combined fixture data : c1
# PASSED
# params_combination.py::test_fixturecetion[c-2] running combined fixture data : c2
# PASSED
# params_combination.py::test_fixturecetion[c-3] running combined fixture data : c3
# PASSED
# params_combination.py::test_fixturecetion[c-4] running combined fixture data : c4
# PASSED
# params_combination.py::test_fixturecetion[d-1] running combined fixture data : d1
# PASSED
# params_combination.py::test_fixturecetion[d-2] running combined fixture data : d2
# PASSED
# params_combination.py::test_fixturecetion[d-3] running combined fixture data : d3
# PASSED
# params_combination.py::test_fixturecetion[d-4] running combined fixture data : d4
# PASSED
