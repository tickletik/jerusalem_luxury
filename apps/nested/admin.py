from django.contrib import admin

from nested.models import * 


from languages.models import LanguageChoice

num_langs = LanguageChoice.objects.filter(is_activated=True).count()

class LowerAdmin(admin.ModelAdmin):
    class DescInline(admin.TabularInline):
        model = Lower.Desc
        max_num = num_langs

    class TitleInline(admin.TabularInline):
        model = Lower.Title
        max_num = num_langs

    #list_display = ['name', 'title', 'description']
    inlines = [DescInline, TitleInline]

class LowerAdminMod(admin.ModelAdmin):
    form = LowerForm
    class DescInline(admin.TabularInline):
        model = Lower.Desc
        max_num = num_langs

    class TitleInline(admin.TabularInline):
        model = Lower.Title
        max_num = num_langs

    #list_display = ['name', 'title', 'description']
    #inlines = [DescInline, TitleInline]


class LowerInline(admin.StackedInline):
    model = Lower
    max_num=1
    

class TopAdmin(admin.ModelAdmin):
    fieldsets = (
            (None, {
                'fields': ['name'],
                'classes': ['whatever'],
                'description': 'testing purposes',
                }),
            )
    inlines = [LowerInline]


admin.site.register(Lower, LowerAdmin)
#admin.site.register(Lower, LowerAdminMod)
admin.site.register(Top, TopAdmin)

