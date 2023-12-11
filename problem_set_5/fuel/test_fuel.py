import fuel

def test_calculation():
    assert fuel.calculate_percentage("4/5") == 80

def test_full():
    assert fuel.calculate_percentage("1/1") == "F"

def test_empty():
    assert fuel.calculate_percentage("0/5") == "E"