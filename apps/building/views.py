from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from django.contrib.admin.views.decorators import staff_member_required 

from jerusalem_luxury.settings import MEDIA_URL, DEBUG

# Create your views here.
import building.models as models
import building.forms as forms


@staff_member_required
def add_block(request):
    """Add buildings and their tenants on a brand new block."""


    if request.method == 'POST':
        f_block = forms.BlockForm(request.POST)

        if f_block.is_valid():
            # don't save the block until the formsets are valid and saved
            block = f_block.save(commit=False)
            block.save()
        
            formset = forms.BuildingFormset(request.POST, request.FILES, instance=block)

            if formset.is_valid():
                rooms = formset.save_all()


                if request.POST.has_key('_continue'): 
                    return redirect('/admin/building/block/%s/' % block.id, block_id=block.id) 
                elif request.POST.has_key('_save'):
                    return redirect('/admin/building/block')
                else:
                    return redirect('/admin/building/block/add/')
            else:
                # didn't work, get rid of this block
                block.delete()
    else:
        f_block = forms.BlockForm()
        formset = forms.BuildingFormset()

    return render_to_response('rentals/edit_buildings.html',
        {
            'opts':models.Block._meta,
            'add':True,
            'app_label':'Buildings',
            'has_change_permission':request.user.is_authenticated,
            
            'f_block':f_block,
            'buildings':formset,

            'MEDIA_URL':MEDIA_URL,
            'DEBUG':DEBUG,
            'request':request,
        }, context_instance = RequestContext(request))
            

@staff_member_required
def edit_block(request, block_id):

    """Edit buildings and their tenants on a given block."""

    block = get_object_or_404(models.Block, id=block_id)

    if request.method == 'POST':
        f_block = forms.BlockForm(request.POST, instance=block)
        formset = forms.BuildingFormset(request.POST, request.FILES, instance=block)
        is_valid = f_block.is_valid(), formset.is_valid()

        if f_block.is_valid():
            f_block.save()

            if formset.is_valid():
                rooms = formset.save_all()

                if request.POST.has_key('_continue'): 
                    return redirect('/admin/building/block/%s/' % block.id, block_id=block.id) 
                elif request.POST.has_key('_save'):
                    return redirect('/admin/building/block')
                else:
                    return redirect('/admin/building/block/add/')
    else:
        f_block = forms.BlockForm(instance=block)
        formset = forms.BuildingFormset(instance=block)


    return render_to_response('rentals/edit_buildings.html',
            {
                'opts':models.Block._meta,
                'app_label':'Buildings',
                'add':False,
                'original':block,
                'has_change_permission':request.user.is_authenticated,

                'f_block':f_block,
                'buildings':formset,

                'MEDIA_URL':MEDIA_URL,
                'DEBUG':DEBUG,
                'request':request,
            }, context_instance = RequestContext(request))
            
