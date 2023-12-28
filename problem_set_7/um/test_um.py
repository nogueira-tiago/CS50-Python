from um import count

def test_basic_case():
    result = count("Hello um world")
    assert result == 1

def test_multiple_occurrences():
    result = count("Um um um")
    assert result == 3

def test_no_occurrence():
    result = count("No umm here")
    assert result == 0
