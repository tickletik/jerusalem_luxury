from jerusalem_luxury.settings import  MEDIA_URL, MEDIA_ROOT
from django.http import HttpResponse
from PIL import Image
from jinja_utils.shortcuts import render_to_response 

# get the base URL from the Site model
from django.contrib.sites.models import Site
current_site = Site.objects.get_current()

def index(request):
    return render_to_response('realty/landing.dtpl', {'MEDIA_URL':MEDIA_URL, 'current_site':current_site, 
        }) 

