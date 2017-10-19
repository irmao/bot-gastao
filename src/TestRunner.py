#!/usr/bin/python
""" Runs all unit tests """

import src.StupidDatabase as StupidDatabase
import src.IntentFunctions as IntentFunctions

def run_unit_tests():
    print("Running unit tests...")
    StupidDatabase.test_reset_get_and_add_value()
    IntentFunctions.test_extract_intent()
    IntentFunctions.test_function_names()
    print("All tests passed! :)")
