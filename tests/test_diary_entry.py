import pytest
from lib.class_diary_entry import *

'''
Gives an error for empty title and contects
'''

def test_error_on_empty_string():
    with pytest.raises(Exception) as e:
        DiaryEntry('', '')
    assert str(e.value) == "Empty diary"

'''
test format returns a formatted entry
'''

def test_format_with_diary_entry():
    diaryentry = DiaryEntry('Day1', 'Good day')
    assert diaryentry.format() == 'Day1: Good day'

'''
assert the number of words in the diary entry
'''

def test_counting_words():
    diaryentry = DiaryEntry('Day one', 'Good Day')
    result = diaryentry.count_words()
    assert result == 4


'''
assert reding time given words per minute 
'''

def test_reading_time():
    diaryentry = DiaryEntry('Day one', 'Good Day')
    result = diaryentry.reading_time(2)
    assert result == 2

'''
Word per minute == 0, raises an error
'''

def test_zero_reading_time():
    diaryentry = DiaryEntry('Day one', 'Good Day')
    with pytest.raises(Exception) as e:
        diaryentry.reading_time(0)
    error = str(e.value)
    assert error == 'Learn to read!'

'''
Given reading time, and free time user have for reading,
return the chunk of text to read in that given time
wpm = 1
free time = 2
reading time returns first two words 
'''

def test_reading_chunk_with_one_wpm_and_two_minutes_free():
    diaryentry = DiaryEntry('Day one', 'one two three four five six')
    result = diaryentry.reading_chunk(1, 2)
    assert result == 'one two'
    
