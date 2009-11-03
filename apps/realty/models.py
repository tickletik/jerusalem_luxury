from django.db import models

from realty_data.models import PropertyType
from realty_data.models import RentalType, SaleType 
from realty_data.models import City, Neighborhood, Region 

class Rent(models.Model):
    asking_price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey('realty_data.RentalType')

    available_from = models.DateField()
    available_to = models.DateField()

    property = models.ForeignKey('Property')


class Sale(models.Model):
    asking_price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey('realty_data.SaleType')

    available_from = models.DateField()
    available_to = models.DateField()

    property = models.ForeignKey('Property')


class Location(models.Model):
    property = models.ForeignKey('Property')
    street = models.CharField(max_length=200, help_text="Please include the street number with the street name")
    zip = models.CharField(verbose_name="Zip/Postal code", max_length=10)
    floor = models.IntegerField(default=0, verbose_name="Floor Number", help_text="All floors are assumed to start at &ldquo;0&rdquo;, that is, 0 is the first floor.  If there is only one floor in the apartment, then leave this at &ldquo;0&rdquo; and in the entry &ldquo;Number of Floors&rdquo; above, leave that at &ldquo;1&rdquo; or &ldquo;0&rdquo;")
    apartment_number = models.CharField(max_length=6, default="None", help_text="If we're dealing with a house or a building without apartment numbers, just leave this as &ldquo;None&rdquo;")

    neighborhood = models.ForeignKey('realty_data.Neighborhood')
    city = models.ForeignKey('realty_data.City')
    region = models.ForeignKey('realty_data.Region')



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
            ('P', 'Private'),
    )

    property = models.ForeignKey("Property")

    bedrooms = models.IntegerField(help_text="Enter # of bedrooms in property")
    bathrooms = models.IntegerField(help_text="Enter # of bathrooms in property")

    #parking_garage = models.BooleanField(verbose_name="Has Parking Garage?")
    #parking_private = models.IntegerField(default=0, verbose_name="Private Parking", help_text="Enter the number of available private parking spaces.  Enter &ldquo;0&rdquo; if there are none")

    parking = models.CharField(max_length=1, default='N', choices=PARKING_CHOICES)
    garden = models.CharField(max_length=1, default='N', choices=GARDEN_CHOICES)

    elevators = models.IntegerField(default=0, help_text="Enter the number of elevators in Property")
    has_elevator_shabbat = models.BooleanField(verbose_name="Has Shabbat Elevator?")

    balcony_width = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="width")
    balcony_length = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="length")

    heating = models.CharField(max_length=1, default='N', choices=HEATING_CHOICES)
    conditioning = models.CharField(max_length=1, default='N', choices=CONDITIONING_CHOICES)



class Property(models.Model):
    class Meta:
        verbose_name_plural="Properties"

    name = models.CharField(max_length=200, help_text="this can be the same as title, but for sanity purposes, please stick to lower case letters connected by underscores. e.g. &ldquo; some_house_in_rechavia_5 &rdquo;")

    title = models.CharField(max_length=200)

    description = models.TextField()

    type = models.ForeignKey('realty_data.PropertyType', verbose_name="Property Type")

    map = models.URLField(blank=True)
    floorplan = models.FileField(upload_to="pdf/floorplans", blank=True)

    number_of_floors = models.IntegerField(default=1, verbose_name="# Floors", help_text="Number of floors in building. Unless the property in question is a cardboard shack on the sidewalk, please at least enter a value of &ldquo;1&rdquo;  :D")

    floor_width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="width")
    floor_length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="length")

    is_available = models.BooleanField(help_text="Is this property still available? If you don't check this box, it won't be displayed on the site.")
    is_featured = models.BooleanField(verbose_name="Display on Home Page?")

    is_rent = models.BooleanField(verbose_name="Is for Rent", help_text="Check this box off if you want this property to be displayed as &ldquo;For Rent&rdquo;")
    is_sale = models.BooleanField(verbose_name="Is for Sale", help_text="Check this box off if you want this property to be displayed as &ldquo;For Sale&rdquo;")


class Images(models.Model):
    property = models.ForeignKey("Property")

    title = models.CharField(max_length=200)
    caption = models.TextField()
    position = models.IntegerField()

    image_large = models.ImageField(upload_to="img/apartments/large")
    image_thumb = models.ImageField(upload_to="img/apartments/thumb", blank=True)
