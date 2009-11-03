from django.contrib import admin

from realty_data.models import * 
from languages.models import LanguageChoice

num_langs = LanguageChoice.objects.filter(is_activated=True).count()


class NeighborhoodAdmin(admin.ModelAdmin):
    class TitleInline(admin.StackedInline):
        model = Neighborhood.Title
        max_num = num_langs

    list_display = ['name', 'city']
    inlines= [TitleInline]

class RegionAdmin(admin.ModelAdmin):
    class TitleInline(admin.StackedInline):
        model = Region.Title
        max_num = num_langs

    list_display = ['name']
    inlines= [TitleInline]

class CityAdmin(admin.ModelAdmin):
    class TitleInline(admin.StackedInline):
        model = City.Title
        max_num = num_langs

    list_display = ['name', 'region']
    inlines= [TitleInline]

class RentalTypeAdmin(admin.ModelAdmin):
    class TitleInline(admin.StackedInline):
        model = RentalType.Title
        max_num = num_langs

    list_display = ['name']
    inlines= [TitleInline]

class SaleTypeAdmin(admin.ModelAdmin):
    class TitleInline(admin.StackedInline):
        model = SaleType.Title
        max_num = num_langs

    list_display = ['name']
    inlines= [TitleInline]

class PropertyTypeAdmin(admin.ModelAdmin):
    class TitleInline(admin.StackedInline):
        model = PropertyType.Title
        max_num = num_langs

    list_display = ['name']
    inlines = [TitleInline]

admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(RentalType, RentalTypeAdmin)
admin.site.register(SaleType, SaleTypeAdmin)
admin.site.register(PropertyType, PropertyTypeAdmin)
