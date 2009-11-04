from django.contrib import admin

from realty.models import * 

from languages.models import LanguageChoice

num_langs = LanguageChoice.objects.filter(is_activated=True).count()

class ImagesInline(admin.StackedInline):
    model = Images
    max_num=1
    verbose_name_plural="Images"

    #class TitleInline(admin.TabularInline):
    #    model = Images.Title
    #    max_num = num_langs
    fieldsets = [
            #(None, {'fields':['name', 'position', 'image_large', 'image_thumb', 'caption']}),
            (None, {'fields':['name', 'title','position', 'image_large', 'image_thumb', 'caption']}),
            ]
    #inlines = [TitleInline]

class ImagesAdmin(admin.ModelAdmin):

    list_display = ['name', 'property']


class LocationAdmin(admin.ModelAdmin):
    pass
    #class StreetInline(admin.StackedInline):
    #    model = Location.Street
    #    max_num = num_langs

    #inlines= [StreetInline]

class LocationInline(admin.StackedInline):
    model = Location
    max_num = 1
    verbose_name_plural="Location/Address"

class AmenitiesInline(admin.StackedInline):
    model = Amenities
    max_num = 1
    verbose_name_plural="House/Apartment Details"

    fieldsets = [
            (None,          {'fields':['bedrooms', 'bathrooms',]}),
            (None,          {'fields':['number_of_floors']}),
            ('Floor Area',  {'fields':[('floor_width', 'floor_length')]}),
            (None,          {'fields':['elevators', 'has_elevator_shabbat', 'parking', 'garden', 'balcony']}),

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

class PropertyAdmin(admin.ModelAdmin):

    class DescInline(admin.TabularInline):
        model = Property.Desc
        max_num = num_langs

    class TitleInline(admin.TabularInline):
        model = Property.Title
        max_num = num_langs

    list_display = ['name']
    fieldsets = [
            #(None,          {'fields':['name', 'title', 'description', 'type', 'is_featured']}),
            (None,          {'fields':['name', 'type', 'is_featured']}),
            ("Availability",   {'fields':['is_active', 'is_available', 'is_rent', 'is_sale']}),
        ]
    inlines = [TitleInline, DescInline, LocationInline, AmenitiesInline, RentalInline, SalesInline, ImagesInline]

admin.site.register(Images, ImagesAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Property, PropertyAdmin)

