import os
import sys
import django.core.handlers.wsgi

sys.path += ['/Users/ronny/Sites', '/opt/projects/django/jerusalem_luxury.git/apps', '/opt/projects/django/apps']

os.environ['DJANGO_SETTINGS_MODULE'] = 'jerusalem_luxury.settings'

application = django.core.handlers.wsgi.WSGIHandler()

