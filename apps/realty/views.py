from django.conf import settings
from django.http import HttpResponse
from PIL import Image
from jinja_utils.shortcuts import render_to_response 

import realty.models as r_models

# get the base URL from the Site model
from django.contrib.sites.models import Site
current_site = Site.objects.get_current()

def index(request):
    return render_to_response('realty/landing.dtpl', {'MEDIA_URL':settings.MEDIA_URL, 'current_site':current_site, 
        }) 

def rentals(request):
    properties = r_models.Property.objects.filter(is_rent=True).filter(is_active=True) 

    for prop in properties:
        prop.display = prop.images_set.order_by('position')[0]

    return render_to_response('realty/rentals.dtpl', {
        'properties':properties,
        'MEDIA_URL':settings.MEDIA_URL, 
        'current_site':current_site, 
        }) 
