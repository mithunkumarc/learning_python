# example 19
from other_code.services import count_service
# mocking objects/functions

import pytest

# install pytest-mock for this example



def test_simple_mocking(mocker):
    """
    pytest-mock provides a fixture for easy, self-cleaning mocking
    """
    #mocking : mock_db_servirce is a mock of db_service
    mock_db_service = mocker.patch("other_code.services.db_service", autospec=True)

    mock_data = [(0, "fake row", 0.0)]

    #changing return value of db_service to [(0, "fake row", 0.0)]
    mock_db_service.return_value = mock_data

    print("\n(Calling count_service with the DB mocked out...)")

    c = count_service("foo") # uses db_service internally

    # check whter db_service(mock) called with input as foo
    mock_db_service.assert_called_with("foo") #

    assert c == 1