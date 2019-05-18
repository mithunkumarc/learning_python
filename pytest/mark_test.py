# example 12
# test cases function can be marked to select and run specific test cases

import pytest

@pytest.mark.database
def test_fake_query():
    '''
    pytest.mark can be used to tag tests for later reference
    '''
    print('test fake query : test case')
    assert True


@pytest.mark.repository
def test_fake_stats_function():
    print('test fake stats function : test case')
    assert True


@pytest.mark.database
@pytest.mark.repository
def test_fake_multi_join_query():
    '''
    test cases can have multiple marks assigned
    '''
    print('test fake multi join query : test case ')
    assert True



# command : specific run test : test_fake_query
# pytest -v mark_test.py::test_fake_query


# command : run all tests with 'query' in their names
# pytest -v -k query



# command : run all tests with "stats" or "join" in their names
# pytest -v -k "stats or join"


# command : with marks
# running test with mark database
# pytest -v -m database

# running test with mark repository
# pytest -v -m repository


# command : to run test with mark database or repository
# pytest -v -m "database or repository"


# Note : database and repository are uses chosen (mark) names