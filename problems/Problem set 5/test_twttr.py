from twttr import shorten
def test_lowercase():
    assert shorten("saugat") == "sgt"

def test_uppercase():
    assert shorten("HiI there Who?") == "H thr Wh?"

def test_numbers():
    assert shorten("CS50e") == "CS50"

def test_punctuation():
    assert shorten("okay?") == "ky?"
