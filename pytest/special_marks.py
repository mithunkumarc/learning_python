# example 13
# skip test
# skip if condition satisfied


import pytest

dev_s3_credentials = None


@pytest.mark.skip
def test_broken_feature():
    '''always skipped'''
    assert False


@pytest.mark.skipif(not dev_s3_credentials,reason='s3 credentials not found')
def test_s3_api():
    '''
    skips if certian condition is met
    because dev_s3_credentials = None, this test also skipped
    '''
    assert True


@pytest.mark.xfail
def test_where_failure_is_acceptable():
    # allows failed assertion( returns xpass if there are no falilure)
    assert True



@pytest.mark.xfail
def test_where_failure_is_accepted():
    '''
    allows failed assertions (returns 'xfail' on failure)
    '''
    assert False


@pytest.mark.xfail(strict=True)
def test_where_failure_is_mandatory():
    '''
    requires failed assertions ! (returns xfail on failure; Fails on pass!)
    this test must fail
    '''
    assert True



# uncomment below line to skip all tests from this module
# pytest.skip('this whole module is problamatic at best !',allow_module_level=True)




# pytest -vs special_marks.py

# special_marks.py::test_broken_feature SKIPPED
# special_marks.py::test_s3_api SKIPPED
# special_marks.py::test_where_failure_is_acceptable XPASS
# special_marks.py::test_where_failure_is_accepted XFAIL
# special_marks.py::test_where_failure_is_mandatory FAILED


# also test module level skip