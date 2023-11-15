import pytest
from lib.include_todo import *

def test_include_todo():
    result = include_todo('This is a #TODO item.')
    assert result == True

def test_not_include_todo():
    result = include_todo('There is nothing to do today.')
    assert result == False

def test_include_todo_empty_string():
    with pytest.raises(Exception) as e:
        include_todo('')
    error_message = str(e.value)
    assert error_message == 'No text to evaluate'