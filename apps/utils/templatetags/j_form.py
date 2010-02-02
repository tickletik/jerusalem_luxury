from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

# for type checking
import django.forms as dforms

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
def do_label_class(value, arg, forarg=None, suffix=":", autoescape=None):

    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    if arg != None:
        result = "<label class=\"%s\">%s%s</label>" % (esc(arg), esc(value), esc(suffix))
    else:
        result = "<label>%s%s</label>" % (esc(value), esc(suffix))

    if forarg != None:
        result = "<label class=\"%s\" for=\"%s\">%s%s</label>" % (esc(arg), esc(forarg), esc(value), esc(suffix))

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
    #{% form_field building.block "div-class" %}
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
    #reg_str = r'\s*("?[\w\-_.: ]+"?)\s+([\w\-_.]+)\s+("?[\w\-_.:]+"?)(\s+("?[\w\-_.:/]+"?)\s+([\w._-]+))?'
    reg_str = r'\s*([\w\-_.]+)\s+("?[\w\-_.: ]+"?)(\s+("?[\w\-_.:/]+"?)\s+([\w._-]+))?'
    m = re.search(reg_str, args)
    if not m:
        raise template.TemplateSyntaxError, "r tag had invalid arguments, %r" % (token.contents.split()[0], m)

    f_instance, d_class =  m.groups()[:2]
    m_url, a_name = m.groups()[3:]

    return FormFieldNode(f_instance, d_class, m_url, a_name)


class FormFieldNode(template.Node):
    def __init__(self, f_instance, d_class, m_url, a_name):
        self.f_instance = f_instance
        self.d_class = d_class
        self.m_url = m_url
        self.a_name = a_name

    def render(self, context):
        m_url = resolve_if_quotes(self.m_url, context) if self.m_url else None
        a_name = resolve_if_quotes(self.a_name, context) if self.a_name else None

        f_instance = template.Variable(self.f_instance).resolve(context)
        d_class = resolve_if_quotes(self.d_class, context)

        d_class += " " + f_instance.name

        # if this is an ImageField, we expect certain things to be displayed
        inst = isinstance(f_instance, dforms.fields.ImageField)
        inst = str(inst)


        if f_instance.field.help_text:
            help_text = """<p class="help">%s</p>""" % f_instance.field.help_text
        else:
            help_text = "" 

        f_label = do_label_class(f_instance.label, "required" if f_instance.field.required else None)

        context_dict = { 'd_class':d_class, 'f_errors':f_instance.errors, 'f_label': f_label, 'f_inst': f_instance, 
                'a_name': a_name,  'media_url':m_url, 'help_text':help_text, }

        if isinstance(f_instance.field, dforms.fields.ImageField):

            result_str = """
                        <div class="%(d_class)s">
                            <div>
                                %(f_errors)s
                                %(f_label)s Currently: <a target="_blank" href="%(media_url)s/%(a_name)s">%(a_name)s</a>
                                <br/>Change: %(f_inst)s
                                %(help_text)s
                            </div>
                        </div>
                """ 

        elif isinstance(f_instance.field, dforms.fields.BooleanField):

            result_str = """
                        <div class="%(d_class)s">
                            <div>
                                %(f_errors)s
                                %(f_inst)s %(f_label)s
                                %(help_text)s
                            </div>
                        </div>
                """
            #f_label = "<label class=\"%s\">%s</label>" % ("vCheckboxLabel required" if f_instance.field.required else "vCheckboxLabel", f_instance.label)
            context_dict['f_label'] = do_label_class(f_instance.label, "vCheckboxLabel required" if f_instance.field.required else "vCheckboxLabel", suffix="" ) 

        elif isinstance(f_instance.field, dforms.fields.DateField):
            
            result_str = """
                        <div class="%(d_class)s">
                            <div>
                                %(f_errors)s
                                %(f_label)s %(f_inst)s
                                %(help_text)s
                            </div>
                        </div>
                """
            f_text = f_instance.as_text()
        
            f_label = do_label_class(f_instance.label, "required" if f_instance.field.required else None, forarg=f_instance.auto_id)

            context_dict['f_label'] = f_label
            context_dict['f_inst'] = f_text[:len(f_text)-2] + " class=\"vDateField\" size=\"10\" />" 


        elif isinstance(f_instance.field, dforms.models.ModelChoiceField):

            reg_str = "<class '([\w_]+).models.([\w_]+)"
            args = str(f_instance.field.queryset.model)

            m = re.search(reg_str, args)

            context_dict['field_id'] = f_instance.auto_id
            context_dict['app_name'] = m.groups()[0]
            context_dict['model_name'] = m.groups()[1].lower()
            #raise Exception("i.model = %r, m = %r" % (str(f_instance.field.queryset.model), m.groups()))

            result_str = """
                        <div class="%(d_class)s">
                            <div>
                                %(f_errors)s
                                %(f_label)s %(f_inst)s
                                
                                <a href="/admin/%(app_name)s/%(model_name)s/add/" class="add-another" id="add_%(field_id)s" onclick="return showAddAnotherPopup(this);"> <img src="/admin/media/img/admin/icon_addlink.gif" width="10" height="10" alt="Add Another"/></a>

                                %(help_text)s
                            </div>
                        </div>""" 


        else:
            result_str = """
                        <div class="%(d_class)s">
                            <div>
                                %(f_errors)s
                                %(f_label)s %(f_inst)s
                                %(help_text)s
                            </div>
                        </div>""" 


       
        return result_str % context_dict


