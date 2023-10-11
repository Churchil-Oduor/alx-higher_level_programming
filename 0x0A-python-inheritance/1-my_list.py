#!/usr/bin/python3

'''The class below inherits from list class
'''


class MyList(list):

    '''The function print_sorted prints the list but in sorted order.
    '''
    def __init__(self):
        self.__list = self

    def print_sorted(self):
        print('{}'.format(self.__list.sort()))
