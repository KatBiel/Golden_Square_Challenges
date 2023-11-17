# Music List Class Design Recipe


## 1. Describe the Problem

Add and see songs that user listened to

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicList:
    # User-facing properties:

    def __init__(self):
        # Parameters: none
        # Side effects:
        #   Initialize an empty list of songs
        pass # No code here yet

    def add(self, song):
        # Parameters:
        #   song: string representing a track name
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the song to the self object
        pass # No code here yet

    def show_list_of_songs(self):
        # Returns:
        #   A list of songs that user has listened to
        # Side-effects:
        #   Throws an exception if list is empty
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Add a song to a list and show the list is updated
"""
musiclist.add('song 1') -> ['song 1']

"""
Add multiple songs to a list and show the list is updated
"""
musiclist.add('song 1') -> ['song 1']
musiclist.add('song 2') -> ['song 1', 'song 2']
musiclist.add('song 3') -> ['song 1', 'song 2', 'song 3']

"""
Raise an error if song is already present in the list
"""
musiclist.add('song 1') -> ['song 1']
musiclist.add('song 1') -> 'Error: song 1 is already in the list'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

