from numb3rs import validate

def test_min():
    assert validate("0.0.0.0") == True

def test_max():
    assert validate("255.255.255.255") == True

def text_str():
    assert validate("dog") == False

def test_all_over():
    assert validate("512.512.512.512") == False

def test_one_over():
    assert validate("1.0.0.500") == False