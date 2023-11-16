from lib.grammar_stats import GrammarStats
import pytest 

def test_check_true():
    grammarstats = GrammarStats()
    assert grammarstats.check('Hello world!') == True

def test_check_false():
    grammarstats = GrammarStats()
    assert grammarstats.check('Hello world:') == False

def test_check_empty_string():
    grammarstats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammarstats.check('')
    error_message = str(e.value)
    assert error_message == 'Error: Empty string'

def tet_percentage_good():
    grammarstats = GrammarStats()
    grammarstats.check('Hello world!')
    grammarstats.check('hello world')
    grammarstats.check('Hello world.')
    assert grammarstats.percentage_good() == 66



    


