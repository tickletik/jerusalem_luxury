from django.contrib import admin

from realty_data.models import * 

class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(RentalType)
admin.site.register(SaleType)
admin.site.register(PropertyType)
