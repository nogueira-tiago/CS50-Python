from validator_collection import checkers

def test_valid_email():
    result = checkers.is_email("user@example.com")
    assert result

def test_invalid_domain():
    result = checkers.is_email("user@")
    assert not result

def test_invalid_characters():
    result = checkers.is_email("user!example.com")
    assert not result

def test_missing_at():
    result = checkers.is_email("userexample.com")
    assert not result