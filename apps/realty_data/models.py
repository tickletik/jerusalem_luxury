from django.db import models

# Create your models here.
    
class PropertyType(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)


class Neighborhood(models.Model):
    name = models.CharField(max_length=200, help_text="you can leave this blank, but if you put anything in it, please keep it as english lowercase with underscores connected words")


class City(models.Model):
    class Meta:
        verbose_name_plural = "Cities"

    name = models.CharField(max_length=200)

class Region(models.Model):
    name = models.CharField(max_length=200)

class RentalType(models.Model):
    class Meta:
        verbose_name="Rental Type"
        verbose_name_plural="Rental Types"

    name = models.CharField(max_length=200)


class SaleType(models.Model):
    class Meta:
        verbose_name="Sales Type"
        verbose_name_plural="Sales Types"

    name = models.CharField(max_length=200)



