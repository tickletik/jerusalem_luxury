from nested.models import *
from languages.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required


#formset imports
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory

def top(request, top_id):

    top_obj = None
    if top_id != None:
        top_obj = Top.objects.get(id=top_id)
    topform = None

def lower2(request, lower_id=None):

    id_lower = lower_id

    m_lower = None
    if id_lower != None:
        m_lower = Lower.objects.get(id=id_lower)


    FormSet_Info = formset_factory(InfoForm, extra=1, can_delete=True) 
    formset_info = FormSet_Info(initial=initial_list(m_lower))
    
    form_lower = LowerForm(instance=m_lower)

    if request.method == 'POST':
        form_lower = LowerForm(request.POST, instance=m_lower)

        if form_lower.is_valid():
            m_lower = form_lower.save(commit=False)
            m_lower.save()


            # note that if form_lower is not valid, then we can't 
            # check out the formset_info
            formset_info = FormSet_Info(request.POST)

            if formset_info.is_valid():

                # set the lower id for both saving, AND for display
                for form in formset_info.forms:
                    if form.cleaned_data.has_key('lower'):
                        form.cleaned_data['lower'] = m_lower
 
                    if form.cleaned_data.has_key('DELETE') and form.cleaned_data['DELETE']:
                        # get ids for title and desc if any, and delete them
                        if form.cleaned_data.has_key('lower_title') and form.cleaned_data['lower_title']:
                            form.cleaned_data['lower_title'].delete()

                        if form.cleaned_data.has_key('lower_desc') and form.cleaned_data['lower_desc']:
                            form.cleaned_data['lower_desc'].delete()

                    else:

                        # we have to put this in an else statement, otherwise after deleting 
                        #   this section will just replace the old values


                        # make sure the object doesn't have blank values in title or lower_title 
    
                        if (form.cleaned_data.has_key('lower_title') and form.cleaned_data['lower_title']) \
                                or (form.cleaned_data.has_key('title') and form.cleaned_data['title']):
                            f_title = TitleForm(data=extract_dict(form.cleaned_data, 't'))
    
                            m_title = f_title.save(commit=False)
                            if form.cleaned_data['lower_title']:
                                m_title.id = form.cleaned_data['lower_title'].id
                            m_title.save()
    
    
    
                        # make sure the object doesn't have blank values in desc or lower_desc 
    
                        if (form.cleaned_data.has_key('lower_desc') and form.cleaned_data['lower_desc']) \
                                or (form.cleaned_data.has_key('desc') and form.cleaned_data['desc']):
                            f_desc = DescForm(data=extract_dict(form.cleaned_data, 'd'))
    
                            m_desc = f_desc.save(commit=False)
                            if form.cleaned_data['lower_desc'] != None:
                                m_desc.id = form.cleaned_data['lower_desc'].id
                            m_desc.save()

                # reload the data
                formset_info = FormSet_Info(initial=initial_list(m_lower))
            

    return render_to_response(
                "admin/nested/lower.html",
                {
                    'form_lower':form_lower,
                    'formset_info':formset_info,
                    'request':request,
                    },
                RequestContext(request, {}),
            )

def lower(request, lower_id=None):

    lower_obj = None
    if lower_id != None:
        lower_obj = Lower.objects.get(id=lower_id)
    lowerform = None


    TitleFSet = modelformset_factory(Lower.Title, can_delete=True, formset=BaseTitleFormSet, max_num=3)
    formset_title = TitleFSet(queryset=Lower.Title.objects.filter(primary=lower_obj), auto_id='id_title_%s', prefix='title')

    DescFSet = modelformset_factory(Lower.Desc, can_delete=True, formset=BaseTitleFormSet, max_num=3)
    formset_desc = DescFSet(queryset=Lower.Desc.objects.filter(primary=lower_obj), auto_id='id_desc_%s', prefix='desc')

    title_instances = None

    if request.method == 'POST':
        lowerform = LowerForm(request.POST, instance=lower_obj)

        if lowerform.is_valid():
            lowerform.save()

        formset_title = TitleFSet(request.POST, auto_id='id_title_%s', prefix='title')

        # if it's all good then save it and reload
        if formset_title.is_valid():
            formset_title.save()
            formset_title = TitleFSet(queryset=Lower.Title.objects.filter(primary=lower_obj), auto_id='id_title_%s', prefix='title')

        formset_desc = DescFSet(request.POST, auto_id='id_desc_%s', prefix='desc')
        if formset_desc.is_valid():
            formset_desc.save()
            formset_desc = DescFSet(queryset=Lower.Desc.objects.filter(primary=lower_obj), auto_id='id_desc_%s', prefix='desc')
        
    else:
        lowerform = LowerForm(instance=lower_obj)
        
    return render_to_response(
            "admin/nested/report.html",
            {
                'lowerform':lowerform,
                'formset_title':formset_title,
                'formset_desc':formset_desc,
                'request':request,
                'instances':title_instances,
                },
            RequestContext(request, {}),
            )

lower2 = staff_member_required(lower2)
lower = staff_member_required(lower)
