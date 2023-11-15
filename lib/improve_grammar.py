def improve_grammar(text):
    if text == '':
        raise Exception('Empty string!')
    if text[-1] in '.!?':
        if text[0].isupper():
            return True
    return False