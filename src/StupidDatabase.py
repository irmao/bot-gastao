#!/usr/bin/python
""" The worst database ever seen in the programming history. 
    Stores values as global variables in memory """

class StupidDatabase:
    def __init__(self):
        self.reset_value()

    def reset_value(self):
        self.current_value = 0

    def get_value(self):
        return self.current_value

    def add_value(self, val):
        self.current_value += val

_internal_database = StupidDatabase()

def get_database():
    return _internal_database

#----------- tests ---------------#
def test_reset_get_and_add_value():
    database = get_database()
    database.reset_value()
    assert database.get_value() == 0
    database.add_value(10)
    database.add_value(8)
    database.add_value(-7)
    assert database.get_value() == 11
    database.reset_value()
    assert database.get_value() == 0