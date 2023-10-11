#!/usr/bin/python3

'''writes a string to a text file in utf-8
and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''
    Args:
        filename: name of the file to be written on.
        text: text to write on the filename.

    Returns:
        number of characters written on the file.
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
    f.close()
    return chars_written
