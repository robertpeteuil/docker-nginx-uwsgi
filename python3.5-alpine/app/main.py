def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World from a default Nginx uWSGI Python 3.5 app in alpine Docker container (default)"]
