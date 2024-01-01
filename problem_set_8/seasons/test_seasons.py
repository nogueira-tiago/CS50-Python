from seasons import days_to_min, convert_to_words, main

def test_days_to_min():
    birth_date = "2000-01-01"
    result = days_to_min(birth_date)
    expected_result = "twelve million, six hundred twenty-three thousand forty minutes"
    assert result == expected_result

def test_convert_to_words():
    minutes = 2482424
    result = convert_to_words(minutes)
    expected_result = "two million, four hundred eighty-two thousand, four hundred twenty-four minutes"
    assert result == expected_result
