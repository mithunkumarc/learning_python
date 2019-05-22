# example 16

# using fixture with mark
from pytest import fixture,mark

@fixture
def class_fixture():
    print('class fixture')


@fixture
def bonus_fixture():
    print('bonus fixture')


@mark.usefixtures('class_fixture','bonus_fixture')
class TestIntermediateClass:

    #this fixture will be called by every test cases inside current class
    @fixture(autouse=True)
    def method_fixture(self):
        print()
        print('autouse method fixture')

    #@mark.usefixtures('method_fixture') # no need of this line
    def test1(self):
        print('running test intermediate test 1')
        assert True

    #@mark.usefixtures('method_fixture') # no need of this line
    def test2(self):
        print('running test intermediate test 2')
        assert True


# output  :
# command : pytest -vs advanced_class_test.py
# advanced_class_test.py::TestIntermediateClass::test1
# autouse method fixture
# class fixture
# bonus fixture
# running test intermediate test 1
# PASSED
# advanced_class_test.py::TestIntermediateClass::test2
# autouse method fixture
# class fixture
# bonus fixture
# running test intermediate test 2
# PASSED
