from django.contrib import admin

from realty.models import * 

class LocationInline(admin.StackedInline):
    model = Location
    max_num = 1
    verbose_name_plural="Location/Address"


class AmenitiesInline(admin.StackedInline):
    model = Amenities
    max_num = 1
    verbose_name_plural="House/Apartment Details"

    fieldsets = [
            (None,          {'fields':['bedrooms', 'bathrooms', 'elevators', 'has_elevator_shabbat', 'parking', 'garden', 'balcony']}),
            ('Heating/Air Conditioning',    {'fields':['heating', 'conditioning']}),

            ]

class RentalInline(admin.StackedInline):
    model = Rent
    max_num = 1
    verbose_name_plural="Rental Information"

class SalesInline(admin.StackedInline):
    model = Sale
    max_num = 1
    verbose_name_plural="Sales Information"

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 3
    verbose_name_plural="Images"

    fieldsets = [
            (None, {'fields':['title', 'position', 'image_large', 'image_thumb']}),
            ('Caption', {'fields':['caption']}),
            ]

class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,          {'fields':['name', 'title', 'description', 'type', 'is_featured']}),
            ("Availability",   {'fields':['is_available', 'is_rent', 'is_sale']}),
            (None,          {'fields':['number_of_floors']}),
            ('Floor Area',  {'fields':[('floor_width', 'floor_length')]}),

        ]
    inlines = [LocationInline, AmenitiesInline, RentalInline, SalesInline, ImagesInline]


admin.site.register(Location)
admin.site.register(Property, PropertyAdmin)

