from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


# for type checking
import django.forms.fields as fields

import re

register = template.Library()



def resolve_if_quotes(var, context):
    result = None 

    if (var[0] == var[-1]) and (var[0] in ('"', "'")):
        result = var.strip(var[0])
    else:
        result = template.Variable(var).resolve(context)

    return result





#----------------------- FILTERS --------------------------


@register.filter(name="label_class")
def do_label_class(value, arg, autoescape=None):

    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    result = "<label class=\"%s\">%s:</label>" % (esc(arg), esc(value))

    return mark_safe(result)

do_label_class.needs_autoescape=True


@register.filter(name='string_form')
def do_string_form(value, arg):
    return arg % value

@register.filter(name='form_value')
def do_form_value(form, arg):
    # filter syntax - {{ form|form_value:'title' }}
    if form.initial.has_key(arg):
        return form.initial[str(arg)]






#----------------------- TAGS --------------------------

@register.tag(name="form_field")
def do_form_field(parser, token):
    #{% form_field "form-row" building.block "required" %}
    #{% form_field "form-row" building.block "required" MEDIA_URL%}
    #{% form_field "form-row css-class2 css-class3" building.block "required" "http://jerusalem_luxury.dev/media/" %}
    try:
        # Splitting by None == splitting by spaces
        #tag_name, d_class, f_instance, l_class = token.split_contents()
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires argumets - %r" % (token.contents.split()[0], token.contents.split())

    #reg_str = r'\s*("?[\w\-_.: ]+"?)\s+([\w\-_.]+)\s+("?[\w\-_.:]+"?)\s*("?[\w\-_.:/]+"?)?\s*([\w._-]+)?'
    reg_str = r'\s*("?[\w\-_.: ]+"?)\s+([\w\-_.]+)\s+("?[\w\-_.:]+"?)(\s+("?[\w\-_.:/]+"?)\s+([\w._-]+))?'
    m = re.search(reg_str, args)
    if not m:
        raise template.TemplateSyntaxError, "r tag had invalid arguments, %r" % (token.contents.split()[0], m)

    d_class, f_instance, l_class = m.groups()[:3]
    m_url, a_name = m.groups()[4:]

    return FormFieldNode(d_class, f_instance, l_class, m_url, a_name)


class FormFieldNode(template.Node):
    def __init__(self, d_class, f_instance, l_class, m_url, a_name):
        self.d_class = d_class
        self.f_instance = f_instance
        self.l_class = l_class
        self.m_url = m_url
        self.a_name = a_name

    def render(self, context):
        m_url = resolve_if_quotes(self.m_url, context) if self.m_url else None
        a_name = resolve_if_quotes(self.a_name, context) if self.a_name else None

        d_class = resolve_if_quotes(self.d_class, context)
        l_class = resolve_if_quotes(self.l_class, context)

        f_instance = template.Variable(self.f_instance).resolve(context)

        # if this is an ImageField, we expect certain things to be displayed
        inst = isinstance(f_instance, fields.ImageField)
        inst = str(inst)

        if m_url and a_name: 
            result_str = """
                        <div class="%(d_class)s">
                            <div>
                                %(f_errors)s
                                %(f_label)s Currently: <a target="_blank" href="%(media_url)s/%(a_name)s">%(a_name)s</a>
                                <br/>Change: %(f_inst)s
                            </div>
                        </div>
                """ 
        else:
            result_str = """
                        <div class="%(d_class)s">
                            <div>
                                %(f_errors)s
                                %(f_label)s %(f_inst)s
                            </div>
                        </div>""" 

        return result_str % { 'd_class':d_class, 
                                'f_errors':f_instance.errors, 
                                'f_label':do_label_class(f_instance.label, l_class),
                                'f_inst': f_instance,
                                'a_name': a_name,  
                                'media_url':m_url,
                                }
