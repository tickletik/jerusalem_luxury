from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


def label_class(value, arg, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    result = "<label class=\"%s\">%s</label>" % (esc(arg), esc(value))
    return mark_safe(result)

label_class.needs_autoescape=True
register.filter('label_class', label_class)


# filter syntax - {{ form|form_initial:'title' }}
def form_initial(form, arg):
    return form.initial[str(arg)]


register.filter('form_initial', form_initial)
    



# tag syntax - {% required_label "somename" %}

def required_label(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, label_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly two arguments" % token.contents.split()[0]

    if not (label_string[0] == label_string[-1] and label_string[0] in ("'", '"')):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    #if not (label_string in ('"', "'")):
    #    raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name

    return RequiredLabelNode(label_string)

class RequiredLabelNode(template.Node):

    def __init__(self, label_string):
        self.label_string = label_string

    def render(self, context):
        full_label = "<label class=\"required\">%s</label>" % self.label_string
        return full_label 


register.tag('required_label', required_label)

