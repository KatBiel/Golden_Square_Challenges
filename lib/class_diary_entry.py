import math
class DiaryEntry:
    def __init__(self, title, contents):
        if title == '' or contents == '':
            raise Exception("Empty diary")
        self.title = title
        self.contents = contents

    def format(self):
        return f'{self.title}: {self.contents}'
    

    def count_words(self):
        return len(self.format().split())


    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('Learn to read!')
        return math.ceil(self.count_words() / wpm)
        

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        contents_list = self.contents.split()
        return ' '.join(contents_list[0:words_user_can_read])