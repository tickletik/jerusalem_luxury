from jerusalem_luxury.settings import BASE_URL, MEDIA_URL, MEDIA_ROOT
from django.http import HttpResponse
#from django.shortcuts import render_to_response

from PIL import Image

from jinja_utils.shortcuts import render_to_response 

def index(request):
    apartment_list = list()

    apartment_path = "apartments/thumbs/bordered/200_150"

    apartment = dict()
    apartment['name'] = '1'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '2'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '3'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '4'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '5'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '6'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '7'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '8'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '9'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '10'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '11'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)

    apartment = dict()
    apartment['name'] = '12'
    apartment['image'] = '%s/%s.png' % (apartment_path, apartment['name'])
    apartment['caption'] = 'Proin at eros non eros adipiscing mollis.' 

    apartment_list.append(apartment)


    return render_to_response('main/main.html', {'MEDIA_URL':MEDIA_URL, 'BASE_URL':BASE_URL, 'apartment_list': apartment_list})
    
def test(request):
    return render_to_response('main/test.html', {})

def testimage(request, image_name):
    image_dir = "img/gallery/home" 
    image_path = "%s/%s/%s.jpg" % (MEDIA_ROOT, image_dir, image_name)

    image = Image.open( image_path )
    response = HttpResponse(mimetype='image/jpg')
    image.save(response, "JPEG")
    return response

