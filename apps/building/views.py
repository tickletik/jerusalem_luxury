from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.contrib.admin.views.decorators import staff_member_required 

from jerusalem_luxury.settings import MEDIA_URL, DEBUG

# Create your views here.
import building.models as models
import building.forms as forms


MainForm = forms.BlockForm
NestedFormset = forms.BuildingFormset
MainModel = models.Block 
nested_labels = {'main':'Block', 'formset':'Building', 'nested':'Title / Description'}
app_label = 'Buildings'
template_object_edit =  'rentals/edit_buildings.html'
template_object_add =  'rentals/edit_buildings.html'

s_continue='/admin/building/block/%s/'
s_save='/admin/building/block'
s_add='/admin/building/block/add/'


@staff_member_required
def add_nestedinline(request):
    """Add buildings and their tenants on a brand new block."""


    if request.method == 'POST':
        form_main = MainForm(request.POST)

        if form_main.is_valid():
            # don't save the m_object until the formsets are valid and saved
            m_object = form_main.save(commit=False)
            m_object.save()
        
            formset = NestedFormset(request.POST, request.FILES, instance=m_object)

            if formset.is_valid():
                rooms = formset.save_all()


                if request.POST.has_key('_continue'): 
                    return redirect(s_continue % m_object.id)
                elif request.POST.has_key('_save'):
                    return redirect(s_save)
                else:
                    return redirect()
            else:
                # didn't work, get rid of this m_object 
                m_object.delete()
    else:
        form_main = MainForm()
        formset = NestedFormset()

    return render_to_response(template_object_add,
        {
            'opts':MainModel._meta,
            'add':True,
            'app_label': app_label,
            'has_change_permission':request.user.is_authenticated,
            
            'form_main':form_main,
            'formset_main':formset,
            'labels':nested_labels,

            'MEDIA_URL':MEDIA_URL,
            'DEBUG':DEBUG,
            'request':request,
        }, context_instance = RequestContext(request))
            

@staff_member_required
def edit_nestedinline(request, object_id):

    """Edit buildings and their tenants on a given block."""
    
    m_object = get_object_or_404(MainModel, id=object_id)

    if request.method == 'POST':
        form_main = MainForm(request.POST, instance=m_object)
        formset = NestedFormset(request.POST, request.FILES, instance=m_object)
        is_valid = form_main.is_valid(), formset.is_valid()

        if form_main.is_valid():
            form_main.save()

            if formset.is_valid():
                rooms = formset.save_all()

                if request.POST.has_key('_continue'): 
                    return redirect(s_continue % m_object.id)
                elif request.POST.has_key('_save'):
                    return redirect(s_save)
                else:
                    return redirect(s_add)
    else:
        form_main = MainForm(instance=m_object)
        formset = NestedFormset(instance=m_object)

    return render_to_response(template_object_edit,
            {
                'opts':MainModel._meta,
                'app_label': app_label,
                'add':False,
                'original':m_object,
                'has_change_permission':request.user.is_authenticated,

                'form_main':form_main,
                'formset_main':formset,
                'labels':nested_labels,


                'MEDIA_URL':MEDIA_URL,
                'DEBUG':DEBUG,
                'request':request,
            }, context_instance = RequestContext(request))
            

add_block=add_nestedinline
edit_block=edit_nestedinline
