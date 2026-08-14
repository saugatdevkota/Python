from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():
    for name in ["Saugat", "Rohan", "John"]:
        assert hello(name) == f"Hello, {name}"
    