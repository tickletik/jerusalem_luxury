from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

def string_form(value, arg):
    return arg % value
register.filter('string_form', string_form)

def label_class(value, arg, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    result = "<label class=\"%s\">%s:</label>" % (esc(arg), esc(value))

    return mark_safe(result)

label_class.needs_autoescape=True
register.filter('label_class', label_class)


# filter syntax - {{ form|form_initial:'title' }}
def form_initial(form, arg):
    if form.initial.has_key(arg):
        return form.initial[str(arg)]


register.filter('form_initial', form_initial)
    

# tag syntax - {% extract_dict some_dict key %}
def extract_dict(parser, token):
    try:
        tag_name, dict_value , key_value = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly three arguments" % token.contents.split()[0]


    return ExtractDictNode(dict_value, key_value)

class ExtractDictNode(template.Node):

    def __init__(self, dict_value, key_value):
        self.dict_value = dict_value
        self.key_value = template.Variable(key_value)

    def render(self, context):

        try:
            actual_key = self.key_value
        except template.VariableDoesNotExist:
            return ''

        return actual_key

register.tag('extract_dict', extract_dict)

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


@register.simple_tag
def format_list(input_list, k):
    return "<ul>\n  <li>%s</li>\n  <li>%s</li>\n</ul>" % (k, "</li>\n <li>".join(input_list))

@register.simple_tag
def dict_key(d_value, k):
    return d_value[k]

import re
@register.tag(name="dict_extract")
def do_dict_extract(parser, token):
    try:
        # Splitting by None == splitting by spaces.
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments - %r" % (token.contents.split()[0], token.contents.split())

    m = re.search(r'(\w+)\s+("?\w+"?)\s+as\s+(\w+)', args)
    if not m:
        raise template.TemplateSyntaxError, "r tag had invalid arguments, %r" % (token.contents.split()[0], m)

    d_arg, k_arg, d_name = m.groups()

    return ExtractDictNode(d_arg, k_arg, d_name)


class ExtractDictNode(template.Node):
    def __init__(self, d_arg, k_arg, d_name):
        self.d_arg = d_arg
        self.k_arg = k_arg
        self.d_name = d_name

    def render(self, context):

        self.d_arg = template.Variable(self.d_arg)
        d_arg = self.d_arg.resolve(context)

        # see if k_arg was surrounded by quotes
        k_arg = self.k_arg
        if (k_arg[0] == k_arg[-1]) and (k_arg[0] in ('"', "'")):
            token = k_arg[0]
            k_arg = self.k_arg.strip(token)
        else:
            self.k_arg  = template.Variable(self.k_arg)
            k_arg = self.k_arg.resolve(context)
        
        context[self.d_name] = d_arg[k_arg]
        return ''


@register.tag(name="content_box")
def do_content_box(parser, token):
    try:
        tag_name, content_heading = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]

    content_heading = template.Variable(content_heading)
    nodelist = parser.parse(('endcontent_box',))
    parser.delete_first_token()

    return FormatContentBoxNode(content_heading, nodelist)

class FormatContentBoxNode(template.Node):
    def __init__(self, content_heading, nodelist):
        self.content_heading = content_heading
        self.nodelist = nodelist

    def render(self, context):
        self.content_heading = self.content_heading.resolve(context)
        content = self.nodelist.render(context)
        return """<div class="content_box"><h1 class="box_heading">%(title)s</h1>%(content)s</div>""" % {'title':self.content_heading, 'content':content,}


@register.tag(name="content_readmore")
def do_content_readmore(parser, token):
    try:
        tag_name, content_heading = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]

    content_heading = template.Variable(content_heading)

    sample_nodelist = parser.parse(('readmore', 'endcontent_readmore',))
    readmore_nodelist = None

    ptoken = parser.next_token()
    if ptoken.contents == 'readmore':
        readmore_nodelist = parser.parse(('endcontent_readmore',))

    parser.delete_first_token()

    return FormatContentReadmoreNode(content_heading, sample_nodelist, readmore_nodelist)

class FormatContentReadmoreNode(template.Node):
    def __init__(self, content_heading, sample_nodelist, readmore_nodelist):
        self.content_heading = content_heading
        self.sample_nodelist = sample_nodelist
        self.readmore_nodelist = readmore_nodelist

    def render(self, context):
        self.content_heading = self.content_heading.resolve(context)
        sample_content = self.sample_nodelist.render(context)

        if self.readmore_nodelist is not None:
            further_content = self.readmore_nodelist.render(context)
            return """
                <div class="content_box">
                    <script type="text/javascript">
                        function show_readmore() {
                            document.getElementById('morelink').style.display='none';
                            document.getElementById('moretext').style.display='block';
                            return false;
                        }
                    </script>

                    <h1 class="box_heading">%(title)s</h1>
                    %(sample_content)s<br />
                    <a id="morelink" href="#" onclick="return show_readmore();">Read More...</a>
                    <div id="moretext" style="display:none">%(further_content)s</div>
                </div>""" % {'title':self.content_heading, 'sample_content':sample_content, 'further_content':further_content,}
        else:
            return """<div class="content_box"><h1 class="box_heading">%(title)s</h1>%(sample_content)s</div>""" % {'title':self.content_heading, 'sample_content':sample_content,}



