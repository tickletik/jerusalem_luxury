from django.http import HttpResponse

# imports to use jinja
from jinja2 import FileSystemLoader, Environment, PackageLoader, ChoiceLoader
from django.conf import settings

# get default mimetype
default_mimetype = getattr(settings, 'DEFAULT_CONTENT_TYPE')

# set the environment
template_dirs = getattr(settings, 'TEMPLATE_DIRS')
env = Environment(loader=FileSystemLoader(template_dirs))

def render_to_response(filename, context={}, mimetype=default_mimetype):
    template = env.get_template(filename)
    rendered = template.render(**context)
    return HttpResponse(rendered, mimetype=mimetype)


