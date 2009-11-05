from django.db import models

from languages.models import ACharField
# Create your models here.

    
class PropertyType(models.Model):
    class Title_P(ACharField):
        primary = models.ForeignKey('PropertyType')
        class Meta:
           verbose_name="Title"

    Title = Title_P

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.name


class Neighborhood(models.Model):
    class Title_N(ACharField):
        primary = models.ForeignKey('Neighborhood')
        class Meta:
           verbose_name="Title"

    Title = Title_N

    name = models.CharField(max_length=200)
    city = models.ForeignKey('City', help_text="which city does this neighborhood belong to?")

    def __unicode__(self):
        return "%s" % self.name


class City(models.Model):
    class Meta:
        verbose_name_plural = "Cities"

    class Title_C(ACharField):
        primary = models.ForeignKey('City')
        class Meta:
           verbose_name="Title"

    Title = Title_C

    name = models.CharField(max_length=200)
    region = models.ForeignKey('Region')

    def __unicode__(self):
        return "%s" % self.name


class Region(models.Model):
    class Title_R(ACharField):
        primary = models.ForeignKey('Region')
        class Meta:
           verbose_name="Title"

    Title = Title_R
        
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.name

class RentalType(models.Model):
    class Meta:
        verbose_name="Rental Type"
        verbose_name_plural="Rental Types"

    class Title_RT(ACharField):
        primary = models.ForeignKey('RentalType')
        class Meta:
           verbose_name="Title"

    Title = Title_RT
        
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.name


class SaleType(models.Model):
    class Meta:
        verbose_name="Sales Type"
        verbose_name_plural="Sales Types"

    class Title_ST(ACharField):
        primary = models.ForeignKey('SaleType')
        class Meta:
           verbose_name="Title"

    Title = Title_ST
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.name



