#!/usr/bin/python

import json

def add_expense_fn(request_json):
    return 'add expense'

def check_balance_fn(request_json):
    return 'check balance'

functions = {
    'AddExpense'   : add_expense_fn,
    'CheckBalance' : check_balance_fn
}

def extract_intent(request_json):
    return request_json['result']['metadata']['intentName']

def get_speech(intent, request_json):
    function_to_call = functions[intent]
    return function_to_call(request_json)


#----------- tests ---------------#
def test_function_names():
    assert functions['AddExpense'] == add_expense_fn
    assert functions['CheckBalance'] == check_balance_fn

def test_extract_intent():
    fsample = open('samples/request.txt', 'r')
    plain_request_json = ''.join(fsample.readlines())
    fsample.close()
    request_json = json.loads(plain_request_json)
    intent = extract_intent(request_json)
    assert intent == 'greetings'