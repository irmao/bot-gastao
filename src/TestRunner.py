#!/usr/bin/python
""" Runs all unit tests """

import src.RequestHandler as RequestHandler
import src.StupidDatabase as StupidDatabase
import src.IntentFunctions as IntentFunctions

def run_unit_tests():
    print("Running unit tests...")
    RequestHandler.test_extract_intent()
    StupidDatabase.test_reset_get_and_add_value()
    IntentFunctions.test_function_names()
    print("All tests passed! :)")
