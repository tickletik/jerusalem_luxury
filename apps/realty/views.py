from django.conf import settings
from django.http import HttpResponse
from PIL import Image
#from jinja_utils.shortcuts import render_to_response 
from django.shortcuts import render_to_response, get_object_or_404, redirect

import realty.models as r_models
import languages.models as l_models

# get the base URL from the Site model
from django.contrib.sites.models import Site
current_site = Site.objects.get_current()
language_curr = l_models.LanguageChoice.objects.filter(is_activated=True)[0]

def index(request):
    return render_to_response('realty/landing.dtpl', {'slideshow_type':'landing', 'MEDIA_URL':settings.MEDIA_URL, 'current_site':current_site,}) 


def listings(request, section):

    if section == 'sales':
        properties = r_models.Property.objects.filter(is_sale=True).filter(is_active=True) 
        section_header = 'Sale'

    elif section == 'rentals':
        properties = r_models.Property.objects.filter(is_rent=True).filter(is_active=True) 
        section_header = 'Rent'

    for prop in properties:
        prop.set_language(language_curr)

    return render_to_response('realty/listings.dtpl', {
        'section': section,
        'section_header': section_header,
        'properties':properties,
        'MEDIA_URL':settings.MEDIA_URL, 
        'current_site':current_site, }) 

def listings_property(request, section, property_id): 

    m_property = get_object_or_404(r_models.Property, id=property_id)
    m_property.set_language(language_curr)

    if section == 'rentals':
        section_header = 'Rent'
    elif section == 'sales':
        section_header = 'Sale'

    return render_to_response('realty/property.dtpl', {
        'section':section,
        'section_header':section_header,
        'property':m_property,
        'MEDIA_URL':settings.MEDIA_URL, 
        'current_site':current_site, 
        }) 

