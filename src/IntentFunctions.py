#!/usr/bin/python

def add_expense_fn():
    print('add expense')

def check_balance_fn():
    print('check balance')

functions = {
    'AddExpense'   : add_expense_fn,
    'CheckBalance' : check_balance_fn
}

def execute_function(intent):
    function_to_call = functions[intent]
    function_to_call()


#----------- tests ---------------#
def test_function_names():
    assert functions['AddExpense'] == add_expense_fn
    assert functions['CheckBalance'] == check_balance_fn
