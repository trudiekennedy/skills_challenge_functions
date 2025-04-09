from lib.text_timer import *
import pytest

def test_find_time_for_200_words():
    result = find_reading_time("Hello " * 200)
    assert result == 1.0

def test_find_time_400_words():
    result = find_reading_time("bananas " * 400)
    assert result == 2.0

def test_find_time_300_words():
    result = find_reading_time("pandas " * 300)
    assert result == 1.5

def test_find_time_empty_string():
    result = find_reading_time("")
    assert result == "No text given: nothing to calculate!"