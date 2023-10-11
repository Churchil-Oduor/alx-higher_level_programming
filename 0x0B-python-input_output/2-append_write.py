#!/usr/bin/python3

'''A function that appends a string at
the end of a text file (UTF8) and returns
the number of characters added.
'''


def append_write(filename="", text=""):
    '''
    Args:
        filename: name of the file.
        text: text to be appended to the string.
    Returns:
        number of characters written in the file.
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        chars_written = f.write(text)
    f.close()
    return chars_written
