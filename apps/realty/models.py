from django.db import models
from django.conf import settings

from utils.methods import comma_me

from PIL import Image


# Title, Rental or Sale, Rented or Sold, Description, Location, Price

class Property(models.Model):

    RENTAL_OR_SALE_CHOICE = (
            ('R', 'Rental'),
            ('S', 'Sale'),
        )

    class Meta:
        verbose_name_plural = 'Properties'


    title = models.CharField(max_length=200)

    rental_or_sale = models.CharField(max_length=1, choices=RENTAL_OR_SALE_CHOICE)
    rented_or_sold = models.BooleanField()

    short_desc = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=300)

    #price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.IntegerField()


    def price_in_dollars(self):
        return "$ " + comma_me(str(self.price))



class Images(models.Model):
    def __unicode__(self):
        if self.property.rental_or_sale == 'R':
            display_title = 'Rental'
        else:
            display_title = 'Sale'
        #return "%s - %s" % (display_title, self.property.title)
        return "somethign"

    def __image_resize__(self, filename, key):
        im = Image.open(filename)

        if settings.RESIZE_TYPE == 'aspect':
            ratio = settings.IMAGE_SIZE[key][0] / float(im.size[0])
            size = settings.IMAGE_SIZE[key][0], int(im.size[1] * ratio)
        elif settings.RESIZE_TYPE == 'plain':
            size = settings.IMAGE_SIZE[key][0], settings.IMAGE_SIZE[key][1]
        
        im = im.resize(size, Image.ANTIALIAS)
    
        # if the height is greater than specified, crop it
        if im.size[1] > settings.IMAGE_SIZE[key][1]:
            im = im.crop(box=(0,0,settings.IMAGE_SIZE[key][0], settings.IMAGE_SIZE[key][1])) 
    
        
        im.save(filename)


    def save(self):
        """
            image_large is a standard image.  It doesn't need to be resized because that's exactly how it's going to be displayed

            or maybe not.

            Anyway, if it's around we can use it as a resized default image for slideshow and thumb
        """
        super(Images, self).save()

        if self.image_thumb:
            self.__image_resize__(self.image_thumb.file.name, 'thumb')
        elif not self.image_thumb and self.image_large:
            # Note: find a better way to extract the name b/c it's always possible that I'll be doing freaky stuff with '/'
            self.image_thumb.save(self.image_large.name.rsplit('/')[-1], self.image_large, save=True)
            self.__image_resize__(self.image_thumb.file.name, 'thumb')

        if self.slideshow:
            self.__image_resize__(self.slideshow.file.name, 'slideshow')
        elif not self.slideshow and self.image_large:
            # Note: find a better way to extract the name b/c it's always possible that I'll be doing freaky stuff with '/'
            self.slideshow.save(self.image_large.name.rsplit('/')[-1], self.image_large, save=True)
            self.__image_resize__(self.slideshow.file.name, 'slideshow')


        if self.image_large:
            self.__image_resize__(self.image_large.file.name, 'large')

    class Meta:
        verbose_name_plural = "Images"


    property = models.ForeignKey("Property")

    in_display = models.BooleanField(verbose_name="To be used as front page display?")
    slideshow = models.ImageField(upload_to="img/slideshow", blank=True, null=True)

    image_large = models.ImageField(upload_to="img/realty/large") 
    image_thumb = models.ImageField(upload_to="img/realty/thumb", blank=True, null=True)


