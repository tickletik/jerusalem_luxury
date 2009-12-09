from django import template

register = template.Library()


@register.inclusion_tag('languages/title_desc.tmpl')
def show_titledesc(formset, label, header_tag="h4"):
    return {'FORMSET':formset, 'LABEL':label, 'header_tag':header_tag }
         
