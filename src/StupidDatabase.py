#!/usr/bin/python
""" The worst database ever seen in the programming history. 
    Stores values as global variables in memory """

class StupidDatabase:
    def __init__(self):
        self.reset_values()

    def reset_values(self):
        self.current_value = 0
        self.expected_expense = 0
        self.payday = 0

    def get_value(self):
        return self.current_value

    def add_value(self, val):
        self.current_value += val

    def get_expected_expense(self):
        return self.expected_expense

    def set_expected_expense(self, val):
        self.expected_expense = val

    def get_payday(self):
        return self.payday

    def set_payday(self, val):
        self.payday = val

_internal_database = StupidDatabase()

def get_database():
    return _internal_database

#----------- tests ---------------#
def test_reset_get_and_add_value():
    database = get_database()
    database.reset_values()
    assert database.get_value() == 0
    assert database.get_expected_expense() == 0
    assert database.get_payday() == 0
    database.add_value(10)
    database.add_value(8)
    database.add_value(-7)
    assert database.get_value() == 11
    database.set_expected_expense(18)
    assert database.get_expected_expense() == 18
    database.set_payday(20)
    assert database.get_payday() == 20
    database.reset_values()
    assert database.get_value() == 0
    assert database.get_expected_expense() == 0
    assert database.get_payday() == 0