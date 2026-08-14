import pytest
from fuel import convert
from fuel import gauge

def test_percent():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_errors():
    with pytest.raises(ValueError):
        assert convert("4/3")
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ValueError):
            assert convert("-1/3")
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


