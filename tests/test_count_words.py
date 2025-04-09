from lib.count_words import *

def test_empty_string():
    result = count_words("")
    assert result == 0

def test_one_word():
    result = count_words("hello")
    assert result == 1