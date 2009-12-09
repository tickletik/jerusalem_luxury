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
            (None, {'fields':['name', 'position', 'image_large', 'image_thumb',] }),
            ]

class ImagesAdmin(admin.ModelAdmin):

    class TitleDescInline(admin.TabularInline):
        model = Images.TitleDesc
        max_num = num_langs

    list_display = ['name', 'property', 'image_large', 'image_thumb', 'position']

    inlines = [TitleDescInline]

class LocationAdmin(admin.ModelAdmin):
    pass

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

    class TitleDescInline(admin.TabularInline):
        model = Property.TitleDesc
        max_num = num_langs

    list_display = ['name']
    fieldsets = [
            #(None,          {'fields':['name', 'title', 'description', 'type', 'is_featured']}),
            (None,          {'fields':['name', 'type', 'is_featured']}),
            ("Availability",   {'fields':['is_active', 'is_available', 'is_rent', 'is_sale']}),
        ]
    inlines = [TitleDescInline, LocationInline, AmenitiesInline, RentalInline, SalesInline, ImagesInline]

admin.site.register(Images, ImagesAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Property, PropertyAdmin)

