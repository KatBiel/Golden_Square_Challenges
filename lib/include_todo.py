def include_todo(text):
    if text == '':
        raise Exception('No text to evaluate')
    return '#TODO' in text
    