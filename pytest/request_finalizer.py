# example 8

# to handle post test process, request finalizer is the best option

# request finalizer will run post test


import pytest

def test_with_safe_cleanup_fixture(safe_fixture):
    print('running test with safe cleanup fixture')
    assert True

@pytest.fixture
def safe_fixture(request):
    '''
    request can also be used to apply post test callbacks
    (this will run if the Fixture itself fails)
    '''
    print() # next line
    print("******PRE TEST********")
    print('began setting up safe fixture')
    request.addfinalizer(safe_cleanup)
    risky_function()


def safe_cleanup():
    print('******POST TEST*********')
    print('cleanup after safe fixture')


def risky_function():
    # uncomment below line to stimulate a failure during fixture setup
    # raise Exception('whoops, i guess that risky function did"t work...')
    print('risky function, totally worth it...')

# command :   pytest -vs request_finalizer.py


# request_finalizer.py::test_with_safe_cleanup_fixture
# ******PRE TEST********
# began setting up safe fixture
# risky function, totally worth it...
# running test with safe cleanup fixture
# PASSED******POST TEST*********
# cleanup after safe fixture
