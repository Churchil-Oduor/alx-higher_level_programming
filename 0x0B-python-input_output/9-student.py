#!/usr/bin/python3

'''Student defines a student.
'''


class Student:
    '''
    Args:
        first_name: first name of student.
        last_name: last name of student.
        age: age of student.

    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''Retrieves a dictionary representation of a Student instance.
    '''

    def to_json(self):
        '''Retrieves a dictionary representation of a student instance.
        '''

        return self.__dict__
