from jerusalem_luxury.settings import BASE_URL, MEDIA_URL, MEDIA_ROOT
from django.http import HttpResponse
#from django.shortcuts import render_to_response

from PIL import Image

from jinja_utils.shortcuts import render_to_response 

def index(request):
    return render_to_response('main/index.html', {'MEDIA_URL':MEDIA_URL})
    
def test(request):
    return render_to_response('main/test.html', {})

def testimage(request, image_name):
    image_dir = "img/gallery/home" 
    image_path = "%s/%s/%s.jpg" % (MEDIA_ROOT, image_dir, image_name)

    image = Image.open( image_path )
    response = HttpResponse(mimetype='image/jpg')
    image.save(response, "JPEG")
    return response

