from bank import value

def test_hello():
    assert value("hello im") == 0

def test_h():
    assert value("hii saugat!") == 20
    assert value("Hii saugat!") == 20

def test_else():
    assert value("Wassup..?") == 100
