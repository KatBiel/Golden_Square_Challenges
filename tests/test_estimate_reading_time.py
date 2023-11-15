import pytest
from lib.estimate_reding_time import *

# reading_time('...200...) -> 1.0

def test_reading_time_200():
    text = ' '.join(['word' for i in range (0, 200)])
    result = reading_time(text)
    assert result == 'The estimated reading time is 1.0 minute.'

# reading_time('...300...) -> 1.5

def test_reading_time_300():
    text = ' '.join(['word' for i in range (0, 300)])
    result = reading_time(text)
    assert result == 'The estimated reading time is 1.5 minutes.'

def test_reding_time_no_text():
    with pytest.raises(Exception) as e:
        reading_time('')
    error_message =str(e.value)
    assert error_message == 'Empty text!'
    