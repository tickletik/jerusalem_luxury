from django.db import models

import realty_data.models as rd_models
import languages.models as l_models

from django.conf import settings

from PIL import Image


class Rent(models.Model):
    property = models.ForeignKey('Property')

    asking_price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(rd_models.RentalType)

    available_from = models.DateField()
    available_to = models.DateField(blank=True, null=True)

    negotiable = models.BooleanField()



class Sale(models.Model):
    property = models.ForeignKey('Property')

    asking_price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(rd_models.SaleType)

    available_from = models.DateField()
    available_to = models.DateField(blank=True, null=True)

    negotiable = models.BooleanField()



class Location(models.Model):

    property = models.ForeignKey('Property')

    street_en = models.CharField(max_length=200, help_text="Please include the street number with the street name", verbose_name="Street (in English)")
    street_he = models.CharField(max_length=200, help_text="Please include the street number with the street name", verbose_name="Street (in Hebrew)")

    zip = models.CharField(verbose_name="Zip/Postal code", max_length=10)
    
    floor = models.IntegerField(default=0, verbose_name="Floor Number", help_text="All floors are assumed to start at &ldquo;0&rdquo;, that is, 0 is the first floor.  If there is only one floor in the apartment, then leave this at &ldquo;0&rdquo; and in the entry &ldquo;Number of Floors&rdquo; above, leave that at &ldquo;1&rdquo; or &ldquo;0&rdquo;")
    
    apartment_number = models.CharField(max_length=6, blank=True, help_text="If we're dealing with a house or a building without apartment numbers, just leave this blank.")

    neighborhood = models.ForeignKey(rd_models.Neighborhood)
    city = models.ForeignKey(rd_models.City)
    region = models.ForeignKey(rd_models.Region)



class Amenities(models.Model):

    HEATING_CHOICES = (
            ('N', 'None'),
            ('P', 'Partial'),
            ('C', 'Central'),
    )

    CONDITIONING_CHOICES = (
            ('N', 'None'),
            ('P', 'Partial'),
            ('C', 'Central'),
    )

    GARDEN_CHOICES = (
            ('N', 'None'),
            ('B', 'Big'),
            ('S', 'Small'),
    )

    PARKING_CHOICES = (
            ('N', 'None'),
            ('G', 'Garage'),
            ('P', 'Reserved Space'),
    )

    BALCONY_CHOICES = (
            ('N', 'None'),
            ('L', 'Large'),
            ('M', 'Medium'),
            ('S', 'Small'),
    )

    FURNISHING_CHOICES = (
            ('N', 'None'),
            ('P', 'Partly'),
            ('F', 'Fully'),
    )

    property = models.ForeignKey("Property")

    bedrooms = models.IntegerField(help_text="Enter # of bedrooms in property")
    bathrooms = models.IntegerField(help_text="Enter # of bathrooms in property")

    number_of_floors = models.IntegerField(default=1, verbose_name="# Floors", help_text="Number of floors in building. Unless the property in question is a cardboard shack on the sidewalk, please at least enter a value of &ldquo;1&rdquo;  :D")

    floor_width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="width")
    floor_length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="length")


    #parking_garage = models.BooleanField(verbose_name="Has Parking Garage?")
    #parking_private = models.IntegerField(default=0, verbose_name="Private Parking", help_text="Enter the number of available private parking spaces.  Enter &ldquo;0&rdquo; if there are none")

    parking = models.CharField(max_length=1, default='N', choices=PARKING_CHOICES)
    garden = models.CharField(max_length=1, default='N', choices=GARDEN_CHOICES)

    number_of_balconies = models.IntegerField(default=0, help_text="Enter # of balconies in property")
    balcony = models.CharField(max_length=1, default='N', choices=BALCONY_CHOICES)

    elevators = models.IntegerField(default=0, help_text="Enter the number of elevators in Property")
    has_elevator_shabbat = models.BooleanField(verbose_name="Has Shabbat Elevator?")

    heating = models.CharField(max_length=1, default='N', choices=HEATING_CHOICES)
    conditioning = models.CharField(max_length=1, default='N', choices=CONDITIONING_CHOICES)

    furnishing = models.CharField(max_length=1, default='N', choices=FURNISHING_CHOICES)


class Property(models.Model):

    def __unicode__(self):
        return "%s" % self.name

    def set_language(self, language_curr):

        titledesc = self.titledesc_property_set.filter(language_choice=language_curr)
        if len(titledesc) > 0: self.titledesc = titledesc[0]

        display = self.images_set.order_by('position')
        if len(display) > 0: self.display = display[0]

        images = self.images_set.order_by('position')
        if len(images) > 0: 
            for im in images:
                im.set_language(language_curr)

            self.images = images

        locations = self.location_set.all()
        if len(locations) > 0: locations = locations[0]

        
        neighborhood = locations.neighborhood.title_n_set.filter(language_choice=language_curr)
        if len(neighborhood) > 0: neighborhood = neighborhood[0].text


        rent = self.rent_set.all()
        if len(rent) > 0: self.rent = self.rent_set.all()[0]

        sale = self.sale_set.all()
        if len(sale) > 0: self.sale = self.sale_set.all()[0]


        amenities = self.amenities_set.all()
        if len(amenities) > 0: self.amenities = amenities[0]
        

    class Meta:
        verbose_name_plural="Properties"

    class TitleDesc_Property(l_models.ATitleDesc):
        primary = models.ForeignKey('Property')
        class Meta:
           verbose_name="Title / Description"

    TitleDesc = TitleDesc_Property

    name = models.CharField(max_length=200, help_text="this can be the same as title, but for sanity purposes, please stick to lower case letters connected by underscores. e.g. &ldquo; some_house_in_rechavia_5 &rdquo;")

    type = models.ForeignKey(rd_models.PropertyType, verbose_name="Property Type")

    map = models.URLField(blank=True, null=True)
    floorplan = models.FileField(upload_to="pdf/floorplans", blank=True, null=True)

    is_available = models.BooleanField(help_text="Is this property still available?")
    is_active = models.BooleanField(help_text="if this box is not checked off, then the property won't be displayed")
    is_featured = models.BooleanField(verbose_name="Display on Home Page?")

    is_rent = models.BooleanField(verbose_name="Is for Rent",
            help_text="Check this box off if you want this property to be displayed as &ldquo;For Rent&rdquo;")
    
    is_sale = models.BooleanField(verbose_name="Is for Sale", 
            help_text="Check this box off if you want this property to be displayed as &ldquo;For Sale&rdquo;")


class Images(models.Model):
    def __unicode__(self):
        return "%s - %s" % (self.name, self.property.name)

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

    def set_language(self, language_curr):
        titledesc = self.titledesc_images_set.filter(language_choice=language_curr)
        if len(titledesc) > 0: self.titledesc = titledesc[0]


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

    class TitleDesc_Images(l_models.ATitleDesc):
        primary = models.ForeignKey('Images')
        class Meta:
           verbose_name="Title / Caption"

    TitleDesc = TitleDesc_Images

    property = models.ForeignKey("Property")

    name = models.CharField(max_length=200)
    position = models.IntegerField()

    in_display = models.BooleanField(verbose_name="To be used as front page display?")

    image_large = models.ImageField(upload_to="img/realty/large") 
    image_thumb = models.ImageField(upload_to="img/realty/thumb", blank=True, null=True)

    slideshow = models.ImageField(upload_to="img/slideshow", blank=True, null=True)

