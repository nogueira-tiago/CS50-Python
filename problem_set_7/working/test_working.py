from working import convert

def test_valid_input():
    result = convert("9:00 am to 5:00 pm")
    assert result == "09:00 to 17:00"

def test_invalid_time_range():
    try:
        convert("3:00 pm to 1:00 pm")
        assert False, "Expected ValueError, but no exception was raised."
    except ValueError as e:
        assert str(e) == "End time is starting before start time.", f"Unexpected error message: {e}"

def test_invalid_time_format():
    try:
        convert("12:60 pm to 2:00 pm")
        assert False, "Expected ValueError, but no exception was raised."
    except ValueError as e:
        assert str(e) == "Invalid time format", f"Unexpected error message: {e}"