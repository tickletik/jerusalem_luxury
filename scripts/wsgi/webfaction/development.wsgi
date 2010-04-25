import os
import sys

sys.path = ['/home/samiah/webapps/django_development', '/home/samiah/webapps/django_development/lib/python2.5', '/home/samiah/webapps/django_development/lib/apps'] + sys.path
from django.core.handlers.wsgi import WSGIHandler


os.environ['DJANGO_SETTINGS_MODULE'] = 'jerusalem_luxury.settings'
application = WSGIHandler()
