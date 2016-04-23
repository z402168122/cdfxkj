# -*- coding: utf-8 -*-

#!/usr/bin/env python

# Run this with
# PYTHONPATH=. DJANGO_SETTINGS_MODULE=testsite.settings testsite/tornado_main.py
# Serves by default at
# http://localhost:8080/hello-tornado and
# http://localhost:8080/hello-django

from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import sys
import os
os.environ.setdefault( "DJANGO_SETTINGS_MODULE", "mysite.settings" )
django.setup()



def main( port ):
    parse_command_line()
    wsgi_app = tornado.wsgi.WSGIContainer( 
      django.core.handlers.wsgi.WSGIHandler() )
    tornado_app = tornado.web.Application( 
      [
        ( '.*', tornado.web.FallbackHandler, dict( fallback = wsgi_app ) ),
        ] )
    server = tornado.httpserver.HTTPServer( tornado_app )
    server.listen( port )
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    try:
        import setproctitle
        setproctitle.setproctitle( 'www:' + sys.argv[1] )
    except ImportError:
        pass
    main( int( sys.argv[1] ) )
