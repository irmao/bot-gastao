#!/usr/bin/python

from MenuStateMachine import MenuStateMachine

class StateMachineHandler:
    _lookup_tags = ['p','table','table','table','table','table','']
    _str = ['Cardapio Unicamp', 'Titulos', 'Almoco', 'Almoco Vegetariano', 'Jantar', 'Jantar Vegetariano', 'Fim.']
    
    @staticmethod
    def get_current_lookup_tag(state):
        return StateMachineHandler._lookup_tags[state]

    @staticmethod
    def match_open_tag(tag, state):
        return tag == StateMachineHandler.get_current_lookup_tag(state)

    @staticmethod
    def to_string(state):
        return StateMachineHandler._str[state]


