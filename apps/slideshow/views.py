from jerusalem_luxury.settings import MEDIA_URL, MEDIA_ROOT
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# imports to use jinja
from jinja2 import FileSystemLoader, Environment, PackageLoader, ChoiceLoader
from django.conf import settings

# get default mimetype
default_mimetype = getattr(settings, 'DEFAULT_CONTENT_TYPE')

# set the environment
template_dirs = getattr(settings, 'TEMPLATE_DIRS')
env = Environment(loader=FileSystemLoader(template_dirs))

# get the base URL from the Site model
from django.contrib.sites.models import Site
current_site = Site.objects.get_current()


import realty.models as r_models

from PIL import Image


def image_list(request, section):

    m_properties = list()
    if section == 'rentals':
        m_properties = r_models.Property.objects.filter(rental_or_sale='R')
    elif section == 'sales':
        m_properties = r_models.Property.objects.filter(rental_or_sale='S')
    else:
        m_properties = r_models.Property.objects.all()

    imagelist = list()
    for prop in m_properties:
        im_set = prop.images_set.filter(in_display=True)

        if len(im_set) > 0:
            imagelist.extend(im_set)
    
    return render_to_response('slideshow/imagelinks.xml', 
    {'MEDIA_URL':MEDIA_URL, 'imagelist':imagelist,})
    

def xml_model(request, section, model_id):

    m_property = get_object_or_404(r_models.Property, id=model_id)
    images = m_property.images_set.all()

    return render_to_response('slideshow/imagelinks.xml', 
        {'MEDIA_URL':MEDIA_URL, 'imagelist':images,})

def render_to_response(filename, context={}, mimetype=default_mimetype):
    template = env.get_template(filename)
    rendered = template.render(**context)
    return HttpResponse(rendered, mimetype=mimetype)
