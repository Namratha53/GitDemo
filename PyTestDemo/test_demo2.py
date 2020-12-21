import pytest

@pytest.mark.skip
def test_secondprogram(setup):
    var = 'Hey'
    assert var == 'Hello', 'Srtings mismatched'

@pytest.mark.smoke
def test_cardprogram1():
    a=2
    b=3
    assert a+b == 5

