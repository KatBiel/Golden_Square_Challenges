class GrammarStats:
    def __init__(self):
        self.count_true = 0
        self.count_false = 0
        self.total_count = self.count_true + self.count_false
  
    def check(self, text):
        if text == '':
            raise Exception('Error: Empty string')
        if text[0].isupper() and text[-1] in '!?.':
            self.count_true += 1
            return True
        else:
            self.count_false += 1
            return False
        
  
    def percentage_good(self):
        result = self.count_true // self.total_count * 100
        return result
        