import pytest

# @pytest.yield_fixture() ------> # this decorator helps to execute method below it ,before and after every other method

#@pytest.fixture()  ----------> # this decorator helps to execute method below it ,before every other method
# this will not be considered as test , this is a fixture

# @pytest.fixture()
# def setup():
#     print("\nthis is at start (from setup())")


@pytest.yield_fixture()
def setup():
    print("\nthis is at beginning (from setup())")
    yield
    print("\n this comes at the end (from setup())")

def test_Method1(setup):
    print(" method 1")

def test_Method2(setup):
    print(" method 2")

