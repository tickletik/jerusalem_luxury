from django.contrib import admin

from realty.models import *

class PropertyAdmin(admin.ModelAdmin):
    class ImageInline(admin.StackedInline):
        model = Images

    inlines=[ImageInline]
    list_display = ['title', 'rental_or_sale', 'rented_or_sold', 'price_in_dollars']
    fieldsets = (
            (None, 
                
                { 
                    'fields': ('title', 'rental_or_sale', 'rented_or_sold', 'short_desc', 'description', 'location', 'price'), 
                    'classes': ['testit'], 
                }
                
            ),
        )

admin.site.register(Property, PropertyAdmin)
