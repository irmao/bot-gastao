#!/usr/bin/python
""" main module """

def wsgi_app(environ, start_response):
    """ Parses the request and sends a reponse """

    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    response_body = environ['wsgi.input'].read(request_body_size)
    yield response_body

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    HTTPD = make_server('localhost', 80, wsgi_app)
    HTTPD.serve_forever()
