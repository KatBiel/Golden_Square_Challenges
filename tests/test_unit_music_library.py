from lib.music_library import MusicLibrary

def test_initially_has_no_tracks():
    library = MusicLibrary()
    assert library.all() == []

def test_search_no_results():
    library = MusicLibrary()
    assert library.search_by_title('Hello') == []