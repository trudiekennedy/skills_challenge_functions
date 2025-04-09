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
    with pytest.raises(Exception) as e:
        find_reading_time("")
    error_message = str(e.value)
    assert error_message == "No text given: nothing to calculate!"