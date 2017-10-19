#!/usr/bin/python
""" Handles the request """

def handle_request(request_json):
    """ Creates and returns a response body from the request json """
    
    fsample = open('samples/response.txt', 'r') 
    response_json = ''.join(fsample.readlines())
    fsample.close()
    print('Response json:', response_json)
    return response_json

