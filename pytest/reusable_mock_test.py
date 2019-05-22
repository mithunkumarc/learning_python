# example 20

from other_code.services import count_service
from pytest import fixture, raises

@fixture
def re_usable_db_mocker(mocker):
    '''
    fixtures can invoke mocker to yield reusable mocks
    '''
    #creating mock for db_service
    mock_db_service = mocker.patch('other_code.services.db_service',autospec=True)
    #changing the return value of
    mock_db_service.return_value = [(0,'fake row',0.0)]
    return mock_db_service



def test_re_usable_mocker(re_usable_db_mocker):
    c = count_service('foo')# uses db_service internally
    #cofirm whter count_service used db_service('foo')
    re_usable_db_mocker.assert_called_with('foo') # check wheter db_service called with foo
    assert c == 1

def test_mocker_with_exception(re_usable_db_mocker):
    #making mock db_service to raise exception
    # db_service raise exception when it called
    re_usable_db_mocker.side_effect = Exception("oh noes!")

    with raises(Exception):
        #no output for below
        #becuase when it call db_service , exception occurs
        count_service('foo')