import plates

test = "aaa111"

def test_start():
    assert plates.start_with_letters(test) == True

def test_length():
    assert plates.valid_length(test) == True

def test_number_end():
    assert plates.numbers_at_end(test) == True

def test_ponctuations():
    assert plates.no_ponctuation(test) == True

def test_validity():
    assert plates.is_valid(test) == True