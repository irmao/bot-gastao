#!/usr/bin/python
""" Handles the request from delegates the required operation to the correct service """
import json

def extract_intent(request_json):
    return request_json['result']['metadata']['intentName']

def handle_request(plain_request_json):   
    request_json = json.loads(plain_request_json)
    print('Request json:', request_json)
    requested_intent = extract_intent(request_json)
    print ('Intent:', requested_intent)
    fsample = open('samples/response.txt', 'r') 
    response_json = ''.join(fsample.readlines())
    fsample.close()
    return response_json.encode('utf-8')

#----------- tests ---------------#
def test_extract_intent():
    fsample = open('samples/request.txt', 'r')
    plain_request_json = ''.join(fsample.readlines())
    fsample.close()
    request_json = json.loads(plain_request_json)
    intent = extract_intent(request_json)
    assert intent == 'greetings'