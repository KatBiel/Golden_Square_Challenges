
class MusicList:
    # User-facing properties:

    def __init__(self):
        self.list = []

    def add(self, song):

        if song in self.list:
            raise Exception('Error: song 1 is already in the list')
        
        self.list.append(song)


    def show_list_of_songs(self):
        if not self.list:
            raise Exception('Error: list is empty')
        return self.list

