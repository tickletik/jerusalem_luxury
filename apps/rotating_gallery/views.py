from jerusalem_luxury.settings import BASE_URL, MEDIA_URL, MEDIA_ROOT
from django.http import HttpResponse

# imports to use jinja
from jinja2 import FileSystemLoader, Environment, PackageLoader, ChoiceLoader
from django.conf import settings

# get default mimetype
default_mimetype = getattr(settings, 'DEFAULT_CONTENT_TYPE')

# set the environment
template_dirs = getattr(settings, 'TEMPLATE_DIRS')
env = Environment(loader=FileSystemLoader(template_dirs))



from PIL import Image

def image_list(request, section):
    # create test data
    imagelist = list()
    
    image = dict()
    image['dir'] = 'home'
    image['name'] = '01'
    image['ext'] = 'jpg'
    image['caption'] = 'Aliquam lectus orci, adipiscing et'
    imagelist.append(image)

    image = dict()
    image['dir'] = 'home'
    image['name'] = '02'
    image['ext'] = 'jpg'
    image['caption'] = 'sodales ac, feugiat non, lacus.'
    imagelist.append(image)

    image = dict()
    image['dir'] = 'home'
    image['name'] = '03'
    image['ext'] = 'jpg'
    image['caption'] = 'Ut dictum velit nec est. Quisque posuere, purus sit amet malesuada blandit,'
    imagelist.append(image)

    image = dict()
    image['dir'] = 'home'
    image['name'] = '04'
    image['ext'] = 'jpg'
    image['caption'] = 'pharetra, urna lectus ultrices est, vel pretium pede '
    imagelist.append(image)

    image = dict()
    image['dir'] = 'home'
    image['name'] = '05'
    image['ext'] = 'jpg'
    image['caption'] = 'sollicitudin tortor. Maecenas volutpat, nisl et dignissim '
    imagelist.append(image)

    image = dict()
    image['dir'] = 'home'
    image['name'] = '06'
    image['ext'] = 'jpg'
    image['caption'] = 'sapien sapien auctor arcu, sed pulvinar felis mi '
    imagelist.append(image)

    #end test data

    gallery_dir = "img/gallery"
    
    return render_to_response('rotating_gallery/image_list.xml', 
        {'MEDIA_URL':MEDIA_URL, 'gallery_dir':gallery_dir, 'imagelist':imagelist,})


def render_to_response(filename, context={}, mimetype=default_mimetype):
    template = env.get_template(filename)
    rendered = template.render(**context)
    return HttpResponse(rendered, mimetype=mimetype)
