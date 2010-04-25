import os
import sys

sys.path = ['/home/samiah/webapps/django_production', '/home/samiah/webapps/django_production/lib/python2.5', '/home/samiah/webapps/django_production/lib/apps'] + sys.path
from django.core.handlers.wsgi import WSGIHandler


os.environ['DJANGO_SETTINGS_MODULE'] = 'jerusalem_luxury.settings'
application = WSGIHandler()
