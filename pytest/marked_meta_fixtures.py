# example 18
# applying fixture to all test in a module

from pytest import fixture,mark

@fixture(scope='module')
def meta_fixture():
    print()
    print('=== begin meta fixture')
    yield
    print()
    print('=== end meta fixture')


# apply this fixture to everything in this module
pytestmark = mark.usefixtures('meta_fixture')

def test_with_meta_fixtures_a():
    print()
    print('running test with meta fixtures a')

def test_with_meta_fixtures_b():
    print()
    print('running test with meta fixtures b')


# marked_meta_fixtures.py::test_with_meta_fixtures_a
# === begin meta fixture
#
# running test with meta fixtures a
# PASSED
# marked_meta_fixtures.py::test_with_meta_fixtures_b
# running test with meta fixtures b
# PASSED
# === end meta fixture
