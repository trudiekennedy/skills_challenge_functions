from lib.check_grammar import *
import pytest

def test_check_for_empty_string():
    with pytest.raises(Exception) as e:
        check_grammar("")
    error_msg = str(e.value)
    assert error_msg == "No text to analyse!"

def test_check_first_letter_isnt_capitalised():
    result = check_grammar("pandas are the best")
    assert result == False

def test_check_first_letter_isnt_capitalised_with_period():
    result = check_grammar("pandas are the best.")
    assert result == False    

def test_check_first_letter_capitalised_with_period():
    result = check_grammar("Pandas are the best.")
    assert result == True

def test_check_first_letter_capitalised_with_exclamation():
    result = check_grammar("Pandas are the best!")
    assert result == True

def test_check_first_letter_capitalised_with_question():
    result = check_grammar("Pandas are the best?")
    assert result == True    

def test_check_capitalised_without_punctuation_ender():
    result = check_grammar("Pandas are the best")
    assert result == False

def test_check_capitalised_with_other_punctuation():
    result = check_grammar("Pandas are best,")
    assert result == False