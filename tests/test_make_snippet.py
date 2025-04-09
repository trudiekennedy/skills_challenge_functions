from lib.make_snippet import *

def test_empty_text():
    result = make_snippet("")
    assert result == ""

def test_five_words():
    result = make_snippet("Hello, how are you today?")
    assert result == "Hello, how are you today?"

def test_six_words():
    result = make_snippet("What are you up to today?")
    assert result == "What are you up to..."