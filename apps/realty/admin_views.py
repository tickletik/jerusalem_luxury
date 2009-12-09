from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.contrib.admin.views.decorators import staff_member_required 

from jerusalem_luxury.settings import MEDIA_URL, DEBUG

# Create your views here.
import realty.models as models
import realty.forms as forms



template_edit =  'realty/admin/edit_property.tmpl'
template_add =  'realty/admin/edit_property.tmpl'
app_label = 'realty'
content_title_property = "Change property"

nested_labels = {'main':'Property', 
        'formset_descs':"Property Title / Description", 
        'formset_images':'Images', 
        'nested':'Image Title and Caption'}

defaultcontext =  {
    'opts':models.Property._meta,
    'app_label': app_label,
    'title': content_title_property,
    'labels':nested_labels,
    'MEDIA_URL':MEDIA_URL,
    'DEBUG':DEBUG, 
}


# redirect urls
r_urls= {
    '_continue': '/t/admin/realty/property/%s/',
    '_add': '/t/admin/realty/property/add/',
    '_save': '/admin/realty/property',
    }


def valid_save(formsetdict):
    """Check for validity and save if valid"""

    validation = reduce(lambda a,b: a and b, [ elem[1].is_valid() for elem in formsetdict.iteritems()])

    if validation:
        formsetdict['formset_images'].save_all()
        [elem[1].save() for elem in formsetdict.iteritems()]

    return validation



@staff_member_required
def add_property(request):
    """Add images and their title/descs on a brand new property."""

    form_property = forms.PropertyForm()

    # use formsetclasses dict to create a dictionary of formset objects
    f_dict = dict( (elem[0], elem[1]()) for elem in forms.formsetclasses.iteritems())

    if request.method == 'POST':
        form_property = forms.PropertyForm(request.POST)


        if form_property.is_valid():
            # don't save the m_property until the formsets are valid and saved
            m_property = form_property.save(commit=False)
            m_property.save()
        
            # use formsetclasses dict to create a dictionary of formset objects
            f_dict = dict( (elem[0], elem[1](request.POST, request.FILES, instance=m_property)) for elem in forms.formsetclasses.iteritems())

        if valid_save(f_dict):
            if request.POST.has_key('_continue'): 
                return redirect(r_urls['_continue'] % m_property.id)
            elif request.POST.has_key('_save'):
                return redirect(r_urls['_save'])
            else:
                return redirect(r_urls['_add'])
        else:
            # didn't work, get rid of this m_property 
            m_property.delete()

    rendercontext = dict()
    rendercontext.update(defaultcontext)
    rendercontext.update(f_dict)
    rendercontext.update(
            {   'add': True,
                'has_change_permission':request.user.is_authenticated,
                'request':request,
                'form_property':form_property, })

    return render_to_response(template_add,
        rendercontext, 
        context_instance = RequestContext(request))
            

@staff_member_required
def edit_property(request, property_id):

    """Edit images and their title/descs on a given property."""
    
    m_property = get_object_or_404(models.Property, id=property_id)

    # create non request.POST forms
    form_property = forms.PropertyForm(instance=m_property)

    # use formsetclasses dict to create a dictionary of formset objects
    f_dict = dict( (elem[0], elem[1](instance=m_property)) for elem in forms.formsetclasses.iteritems())

    # now run through it if we actually have post data
    if request.method == 'POST':
        form_property = forms.PropertyForm(request.POST, instance=m_property)

        # use formsetclasses dict to create a dictionary of formset objects
        f_dict = dict( (elem[0], elem[1](request.POST, request.FILES, instance=m_property)) for elem in forms.formsetclasses.iteritems())

        if form_property.is_valid():
            form_property.save()

        if valid_save(f_dict):
            if request.POST.has_key('_continue'): 
               return redirect(r_urls['_continue'] % m_property.id)
            elif request.POST.has_key('_save'):
               return redirect(r_urls['_save'])
            else:
               return redirect(r_urls['_add'])

    rendercontext = dict()
    rendercontext.update(defaultcontext)
    rendercontext.update(f_dict)
    rendercontext.update({ 'add':False,
                'original':m_property,
                'has_change_permission':request.user.is_authenticated,
                'request':request,
                'form_property':form_property, })

    return render_to_response(template_edit,
            rendercontext, 
            context_instance = RequestContext(request))
            

