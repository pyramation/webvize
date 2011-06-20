import os, sys

sys.path.append('/var/www/webvize.com/webvize')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
