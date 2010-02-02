from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

# for type checking
import django.forms as dforms

import re

register = template.Library()

locale.setlocale(locale.LC_ALL, '')
register = template.Library()
 
@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)


@register.filter(name='testit')
def testit(value, arg):
    return 'blah'

@register.filter(name="float_format")
def float_format(value, seperator=u'.'):
    decimal_points = 3
    value = str(value)
    if len(value) <= decimal_points:
        return value
    # say here we have value = '12345' and the default params above
    parts = []
    while value:
        parts.append(value[-decimal_points:])
        value = value[:-decimal_points]
    # now we should have parts = ['345', '12']
    parts.reverse()
    # and the return value should be u'12.345'
    return seperator.join(parts)




