#!/usr/bin/python
""" Handles the request from delegates the required operation to the correct service """
import json
import src.IntentFunctions as IntentFunctions

def handle_request(plain_request_json):   
    request_json = json.loads(plain_request_json)
    fsample = open('samples/response_empty.txt', 'r') 
    response_json = json.loads(''.join(fsample.readlines()))
    fsample.close()
    requested_intent = IntentFunctions.extract_intent(request_json)
    speech = IntentFunctions.get_speech(requested_intent, request_json)
    response_json['speech'] = speech.message
    response_json['displayText'] = speech.message
    response_json['contextOut'] = speech.contextOut
    return json.dumps(response_json).encode('utf-8')
