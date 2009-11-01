from django.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)

class City(models.Model):
    name = models.CharField(max_length=200)

class Region(models.Model):
    name = models.CharField(max_length=200)


class Location(models.Model):
    street = models.CharField(max_length=200)
    zip = models.CharField(max_length=10)
    floor = models.IntegerField()
    apartment_number = models.CharField(max_length=6)

    neighborhood = models.ForeignKey('Neighborhood')
    city = models.ForeignKey('City')
    region = models.ForeignKey('Region')


class RentalType(models.Model):
    name = models.CharField(max_length=200)


class SaleType(models.Model):
    name = models.CharField(max_length=200)


class Rent(models.Model):
    asking_price = models.DecimalField(decimal_places=2)
    type = models.ForeignKey('RentalType')

    available_from = models.DateField()
    available_to = models.DateField()

    property = models.ForeignKey('Property')


class Sale(models.Model):
    asking_price = models.DecimalField(decimal_places=2)
    type = models.ForeignKey('SaleType')

    available_from = models.DateField()
    available_to = models.DateField()

    property = models.ForeignKey('Property')


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

    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    parking_garage = models.BooleanField()
    parking_private = models.IntegerField()

    garden_area = models.DecimalField(decimal_places=2)

    elevators = models.IntegerField()
    has_elevator_shabbat = models.BooleanField()

    balcony_area = models.DecimalField(decimal_places=2)

    heating = models.CharField(max_length=1, choices=HEATING_CHOICES)
    conditioning = models.CharField(max_length=1, choices=CONDITIONING_CHOICES)



class Property(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    map = models.URLField()
    floorplan = models.FileField(upload_to="pdf/floorplans", blank=True)

    location = models.ForeignKey('Location')
    amenities = models.ForeignKey('Amenities')

    number_of_floors = models.IntegerField()
    area = models.DecimalField(decimal_places=2)

    is_available = models.BooleanField()
    is_featured = models.BooleanField()


class Images(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    caption = models.TextField()
    position = models.IntegerField()

    image_large = models.ImageField(upload_to="img/apartments/large")
    image_thumb = models.ImageField(upload_to="img/apartments/thumb")
