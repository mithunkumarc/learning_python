# example number 3
# not everything can be expressed as simple assertion

# purposefully checking whether code raises exception or not
import pytest
def test_div_by_zero():
    '''   pytest.raises can assert that exceptions are raised (catching them)'''
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0
        #test fails when  x = 1 / 1 , because code doesn't raise Error
        print(f'{x}')



# purposefully asserting exception : keyerror, (key not found)
def test_keyerror_details():
    '''the raised exception can be referenced and further inspected or asserted'''
    my_map = {"foo":"bar"}

    with pytest.raises(KeyError) as ke:
        baz = my_map['baz'] # no key called baz, so raises KeyError, referenced by ke
        # eg : wrong username/password must raise, this code can be used to test whether code raises error or not
        print(f"found baz : {baz}")
    print(f'raised : {ke}')



#  pytest.approx to help assert that our two values are "approximately" equal,
def test_approximate_matches():
    '''pytest.approx used to assert approximate numerical equality'''
    assert (0.1001 + 0.2) == pytest.approx(0.3,rel=1e-3) # dont care after 3 decimals values (rel : ralative?)

# pytest -q test_special_assertions.py













