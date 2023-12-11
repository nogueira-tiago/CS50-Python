from bank import confirmation

def test_hello():
    assert confirmation("hello") == "$ 0"

def test_h():
    assert confirmation("hi") == "$ 20"

def test_else():
    assert confirmation("aoba") == "$ 100"