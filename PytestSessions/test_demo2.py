import pytest
@pytest.mark.roger
def test_m1():
    a = 2
    b = 2
    assert a == b, "test case passed"
    assert b == a + 1, "test case failed"
@pytest.mark.roger
def test_m2():
    a = 3
    b = 4
    assert a+b == 7, "test case passed"
@pytest.mark.that
def test_m3():
    assert 100 == 100, "test case passed"