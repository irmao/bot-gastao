#!/usr/bin/python
""" main module """

from src.HandleRequest import handle_request

def wsgi_app(environ, start_response):
    """ Parses the request and sends a reponse """

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size)
    response_body = handle_request(request_body.decode('utf-8'))
    yield response_body.encode('utf-8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    HTTPD = make_server('localhost', 80, wsgi_app)
    HTTPD.serve_forever()
