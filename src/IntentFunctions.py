#!/usr/bin/python

import json
import src.StupidDatabase as StupidDatabase

def extract_intent(request_json):
    return request_json['result']['metadata']['intentName']

def extract_value(request_json):
    return int(request_json['result']['parameters']['value'])

def add_expense_fn(request_json):
    value = extract_value(request_json)
    StupidDatabase.get_database().add_value(value)
    message = ''
    if value == 0:
        message = 'Me poupe! Isso não faz diferença nenhuma'
    elif value < 0:
        message = 'Ok! Subtraí ' + str(-value) + ' reais do seu saldo'
    else:
        message = 'Ok! Adicionei ' + str(value) + ' reais no seu saldo'
    return message

def check_balance_fn(request_json):
    value = StupidDatabase.get_database().get_value()
    message = ''
    if value == 0:
        message = 'Sua conta está ZERADA. Pelo menos você não deve nada :)'
    elif value < 0:
        message = 'Você deve ' + str(-value) + ' reais'
    else:
        message = 'Você possui ' + str(value) + ' reais na sua conta'
    return message

functions = {
    'AddExpense'   : add_expense_fn,
    'CheckBalance' : check_balance_fn
}

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
    assert intent == 'CheckBalance'