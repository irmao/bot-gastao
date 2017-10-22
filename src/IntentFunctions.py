#!/usr/bin/python

import json
import src.StupidDatabase as StupidDatabase
#import src.Classifier as Classifier

def create_context_obj(context_name):
    return {'name': context_name, 'lifespan': 1}

def extract_intent(request_json):
    return request_json['result']['metadata']['intentName']

def extract_value(request_json):
    return int(request_json['result']['parameters']['value'])

def extract_contexts(request_json):
    return request_json['result']['contexts']

def extract_input_sentence(request_json):
    return request_json['result']['resolvedQuery']

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
    return {'message': message, 'contextOut' : []}

def check_balance_fn(request_json):
    value = StupidDatabase.get_database().get_value()
    message = ''
    if value == 0:
        message = 'Sua conta está ZERADA. Pelo menos você não deve nada :)'
    elif value < 0:
        message = 'Você deve ' + str(-value) + ' reais'
    else:
        message = 'Você possui ' + str(value) + ' reais na sua conta'
    return {'message': message, 'contextOut' : []}

def greeting_fn(request_json):
    message = 'Oi, tudo bem? Eu posso te ajudar a controlar os seus gastos. Mas para isso, preciso fazer algumas perguntas, pode ser? Vamos lá. Quanto você se dispõe a gastar em um mês?'
    return {'message': message, 'contextOut': [create_context_obj('waiting-expected-expense')]}

def add_expected_expense_fn(request_json):
    value = extract_value(request_json)
    StupidDatabase.get_database().set_expected_expense(value)
    message = 'Ok! Você pretende gastar ' + str(value) + ' por mês, vou te ajudar a cumprir essa meta. Que dia do mês você recebe seu salário?'
    return {'message': message, 'contextOut': [create_context_obj('waiting-payday')]}

def add_payday_fn(request_json):
    value = extract_value(request_json)
    StupidDatabase.get_database().set_payday(value)
    message = 'Você recebe dia ' + str(value) + '. Anotado! Agora quando gastar alguma coisa, por favor me informe. Eu irei te avisar se seu dinheiro estiver acabando e o dia do pagamento estiver longe. E se quiser checar o seu saldo, só perguntar! :)'
    return {'message': message, 'contextOut': []}

def default_fallback_fn(request_json):
    input_sentence = extract_input_sentence(request_json)
    #message = Classifier.classify(input_sentence)
    message = 'Classifier not imported'
    return {'message': message, 'contextOut': []}

functions = {
    'AddExpense'   : add_expense_fn,
    'CheckBalance' : check_balance_fn,
    'Greeting'     : greeting_fn,
    'AddExpectedExpense' : add_expected_expense_fn,
    'AddPayday'    : add_payday_fn,
    'Default Fallback Intent' : default_fallback_fn
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