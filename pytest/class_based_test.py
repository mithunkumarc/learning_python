# example 15

class TestSimpleClass:
    '''
    classes can still be used to organize collection of test cases
    with each test being a methiod on the class, rather than a statndlone function
    '''
    x = 1
    y = 2

    def regular_method(self):
        print('this is regular method. non test case method')

    def test_two_checking_method(self):
        print('running class based test')
        assert self.x == 1
        assert self.y == 2