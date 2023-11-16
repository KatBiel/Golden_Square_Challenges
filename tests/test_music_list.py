from lib.music_list import MusicList
import pytest 

"""
Add a song to a list and show the list is updated
"""
def test_add_song():
    musiclist = MusicList()
    musiclist.add('song 1')
    assert musiclist.list == ['song 1']

"""
Add multiple songs to a list and show the list is updated
"""
def test_multiple_songs():
    musiclist = MusicList()
    musiclist.add('song 1')
    musiclist.add('song 2')
    musiclist.add('song 3')
    assert musiclist.list == ['song 1', 'song 2', 'song 3']

"""
Raise an error if song is already present in the list
"""
def test_already_in_list():
    musiclist = MusicList()
    with pytest.raises(Exception) as e:
        musiclist.add('song 1')
        musiclist.add('song 1')
    error = str(e.value)
    assert error == 'Error: song 1 is already in the list'

def test_show_list():
    musiclist = MusicList()
    musiclist.add('song 1')
    musiclist.add('song 2')
    assert musiclist.show_list_of_songs() == ['song 1', 'song 2']

def test_show_empty_list():
    musiclist = MusicList()
    with pytest.raises(Exception) as e:
        musiclist.show_list_of_songs()
    error = str(e.value)
    assert error == 'Error: list is empty'
