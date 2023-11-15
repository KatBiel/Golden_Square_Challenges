def reading_time(text):
    word_count = len(text.split())

    if word_count == 0:
        raise Exception('Empty text!')
    
    estimated_reading_time = word_count/200
    
    if estimated_reading_time <= 1:
        return f'The estimated reading time is {estimated_reading_time} minute.'
    else:
        return f'The estimated reading time is {estimated_reading_time} minutes.'
