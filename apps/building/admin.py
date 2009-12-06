from django.contrib import admin

from building.models import *
from building.forms import *

num_langs = LanguageChoice.objects.filter(is_activated=True).count()

class BlockAdmin(admin.ModelAdmin):
    pass

class BuildingAdmin(admin.ModelAdmin):
    class TenantInline(admin.TabularInline):
        model = Tenant
        max_num = num_langs

    inlines = [TenantInline]

admin.site.register(Block, BlockAdmin)
admin.site.register(Building, BuildingAdmin)

