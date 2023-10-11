#!/usr/bin/python3

'''function that reads a text file (UTF8)
and prints it to stdout.
'''


def read_file(filename=""):
    '''reads the contents of a file and prints them on stdout.
    Args:
        filename: name of the file.
    '''
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()

    print(read_data)
    f.close()
