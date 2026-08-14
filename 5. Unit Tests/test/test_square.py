from calculate_square import square
import pytest
"""
def main():
    square_test()

def square_test():
    # if square(2) != 2:
    #     print("Test failed: square of 2 should be 4")
    # if square(3) != 9:
    #     print("Test failed: square of 3 should be 9")
    try:
        assert square(2) == 4
    except AssertionError:
        print("Test failed: square of 2 should be 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed: square of 3 should be 9")

if __name__ == "__main__":
    main()
"""

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("Word")

