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
    'DEBUG':DEBUG, }

s_continue='/t/admin/realty/property/%s/'
s_add='/t/admin/realty/property/add/'
s_save='/admin/realty/property'


def is_validity(formsetdict):

    validation = reduce(lambda a,b: a and b, [ elem[1].is_valid() for elem in formsetdict.iteritems()])

    if validation:
        formsetdict['formset_images'].save_all()
        formsetdict['formset_descs'].save()
        formsetdict['formset_location'].save()
        formsetdict['formset_amenities'].save()

    return validation



@staff_member_required
def add_property(request):
    """Add images and their title/descs on a brand new property."""


    if request.method == 'POST':
        form_property = forms.PropertyForm(request.POST)

        # it's necessary to use validation = False
        # because all the formsets require an instance of models.Property and as we are in an "add" method
        # that hasn't yet been created yet.  So first  
        validation = False
        f_dict = dict()

        if form_property.is_valid():
            # don't save the m_property until the formsets are valid and saved
            m_property = form_property.save(commit=False)
            m_property.save()
        
            f_dict['formset_images'] = forms.ImagesFormset(request.POST, request.FILES, instance=m_property)
            f_dict['formset_descs'] = forms.PropertyTitleDescFormset(request.POST, instance=m_property)
            f_dict['formset_location'] = forms.LocationFormset(request.POST, instance=m_property)
            f_dict['formset_amenities'] = forms.AmenitiesFormset(request.POST, instance=m_property)

            validation = is_validity(f_dict)

        if validation:
            if request.POST.has_key('_continue'): 
                return redirect(s_continue % m_property.id)
            elif request.POST.has_key('_save'):
                return redirect(s_save)
            else:
                return redirect()
        else:
            # didn't work, get rid of this m_property 
            m_property.delete()
    else:
        form_property = forms.PropertyForm()
        f_dict['formset_images'] = forms.ImagesFormset()
        f_dict['formset_descs'] = forms.PropertyTitleDescFormset()
        f_dict['formset_location'] = forms.LocationFormset()
        f_dict['formset_amenities'] = forms.AmenitiesFormset()

    rendercontext = dict()
    rendercontext.update(defaultcontext)
    rendercontext.update(f_dict)
    rendercontext.update({ 'add':False,
                'original':m_property,
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
    f_dict = dict()

    if request.method == 'POST':
        form_property = forms.PropertyForm(request.POST, instance=m_property)
        f_dict['formset_images'] = forms.ImagesFormset(request.POST, request.FILES, instance=m_property)
        f_dict['formset_descs'] = forms.PropertyTitleDescFormset(request.POST, instance=m_property)
        f_dict['formset_location'] = forms.LocationFormset(request.POST, instance=m_property)
        f_dict['formset_amenities'] = forms.AmenitiesFormset(request.POST, instance=m_property)


        is_valid = form_property.is_valid(), f_dict['formset_images'].is_valid()


        validation = False
        if form_property.is_valid():
            form_property.save()

            validation = is_validity(f_dict)

            #if is_validity(f_dict):
            #    f_dict['formset_images'].save_all()
            #    f_dict['formset_descs'].save()
            #    f_dict['formset_location'].save()
            #    f_dict['formset_amenities'].save()
            #    validation = True

        if validation:
            if request.POST.has_key('_continue'): 
               return redirect(s_continue % m_property.id)
            elif request.POST.has_key('_save'):
               return redirect(s_save)
            else:
               return redirect(s_add)
    else:
        form_property = forms.PropertyForm(instance=m_property)
        f_dict['formset_images'] = forms.ImagesFormset(instance=m_property)
        f_dict['formset_descs'] = forms.PropertyTitleDescFormset(instance=m_property)
        f_dict['formset_location'] = forms.LocationFormset(instance=m_property)
        f_dict['formset_amenities'] = forms.AmenitiesFormset(instance=m_property)

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
            

