from jar import Jar

def test_capacity():
    try:
        Jar(capacity = -5)
        assert False, "Expected ValueError, but no exception was raised."
    except ValueError as e:
        assert str(e) == "Capacity can't be negative.", f"Unexpected error message: {e}"

def test_deposit_exceeding_capacity():
    jar = Jar(capacity=5)
    try:
        jar.deposit(8)
        assert False, "Expected ValueError, but no exception was raised."
    except ValueError as e:
        assert str(e) == "Jar capacity exceeded.", f"Unexpected error message: {e}"


def test_negative_deposit():
    jar = Jar()
    try:
        jar.deposit(-3)
        assert False, "Expected ValueError, but no exception was raised."
    except ValueError as e:
        assert str(e) == "Deposit can't be negative.", f"Unexpected error message: {e}"

def test_withdraw_more_than_size():
    jar = Jar()
    try:
        jar.withdraw(5)
        assert False, "Expected ValueError, but no exception was raised."
    except ValueError as e:
        assert str(e) == "No cookie to withdraw.", f"Unexpected error message: {e}"

def test_negative_withdraw():
    jar = Jar()
    try:
        jar.withdraw(-3)
        assert False, "Expected ValueError, but no exception was raised."
    except ValueError as e:
        assert str(e) == "Deposit can't be negative.", f"Unexpected error message: {e}"
