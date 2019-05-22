# example 17

# meta_fixture run only once around tests
from pytest import fixture, mark

class ExpensiveClass():
    def __init__(self):
        print("(Initializing ExpensiveClass instance...)")
        import time
        time.sleep(0.2)
        print("(ExpensiveClass instance complete!)")


    def __str__(self):
        return '*i am expensive class*'

@fixture(scope="module", autouse=True)
def scoped_fixture():
    """
    Scoping affects how often fixtures are (re)initialized
    """
    print("\n(Begin Module-scoped fixture)") # before test case
    yield ExpensiveClass() # same object for all 50 iteration
    print("\n(End Module-scoped fixture)") # after test case


@mark.parametrize("x", range(1, 51))
def test_scoped_fixtures(x,scoped_fixture): # get Expensive class
    """
    A (hopefully fast!) test, to be run with fifty different parameters...
    """
    print()
    print(scoped_fixture)
    print("\n   Running test_scoped_fixture",x)


# pytest -vs scoped_meta_fixtures_test.py
# output :
#(Begin Module-scoped fixture)
# *i am expensive class*
# Running test_scoped_fixture 1
#
# *i am expensive class*
# Running test_scoped_fixture 2
#
# .
# .
# *i am expensive class*
# Running test_scoped_fixture 1
#(End Module-scoped fixture)


