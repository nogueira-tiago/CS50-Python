from twttr import message_twttr

def test_message():
    assert message_twttr("monday") == "mndy"
