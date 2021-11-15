"""
WSGI config for dbmkt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

def application(env, start_response):
        print(sys.prefix)
        print(sys.path)
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"Hello World"]


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbmkt.settings')

#application = get_wsgi_application()
