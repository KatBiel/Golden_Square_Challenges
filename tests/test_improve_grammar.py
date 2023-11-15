import pytest
from lib.improve_grammar import *

# improve_grammar('This is a sentence') -> False
# improve_grammar('This is a sentence.') -> True

def test_improve_grammar_correct_sentence_one():
    result = improve_grammar('This is a sentence.')
    assert result == True

def test_improve_grammar_correct_sentence_two():
    result = improve_grammar('This is a sentence?')
    assert result == True

def test_improve_grammar_incorrect_sentence_one():
    result = improve_grammar('this is a sentence!')
    assert result == False

def test_improve_grammar_incorrect_sentence_two():
    result = improve_grammar('This is a sentence:')
    assert result == False

def test_improve_grammar_empty_string():
    with pytest.raises(Exception) as e:
        improve_grammar('')
    error_message = str(e.value)
    assert error_message == 'Empty string!'