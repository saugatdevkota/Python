from plates import is_valid

def test_start():
    assert is_valid("CS50") == True
    assert is_valid("s76") == False


def test_max():
    assert is_valid("HelloIm") == False

def test_mnumbers():
    assert is_valid("Ss7D") == False
    assert is_valid("su07") == False


def test_periods():
    assert is_valid("Hii Im") == False
