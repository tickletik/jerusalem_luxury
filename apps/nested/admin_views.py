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

    form_lower = None

    """
    TODO: Use the model formsets from below! for Title and Desc to populate the info formset!
    NOTE: make sure to keep the initial value of 'id_lower' set to the lower object id
    """
    FormSet_Info = formset_factory(InfoForm, extra=2) 
    formset_info = FormSet_Info()
    #formset_info = initialize_formset(FormSet_Info, initial_list(m_lower, 2)) 
    

    if request.method == 'POST':
        form_lower = LowerForm(request.POST, instance=m_lower)

        if form_lower.is_valid():
            form_lower.save()

            
        """
        # for each form in the formsets filled out:
        # something like the following:
        initial_forms = int(request.POST['form-INITIAL_FORMS'][0])
        total_forms = int(request.POST['form-TOTAL_FORMS'][0])
        

        formset_info = FormSet_Info(request.POST)
        if formset_info.is_valid():
            for f in formset_info.forms:
                f.cleaned_data  # do something with this

        # NOTE: ALTHERNATIVELY YOU CAN USE THE FOLLOWING---
        [form.cleaned_data for form in formset_info.forms]

        # might have to change based on initial vs. total, eg. 
        # range(0, total_forms - initial_forms) ?????  probably not.

        for form_num in range(0, total_forms):
            form_prefix = 'form-' + str(form_num)

            # get the general data from the request object
            dict_request = transfer_dict(request.POST, form_prefix)


            # extract data for title and process
            data_t = extract_dict(dict_request, 't')

            # create a generic form_t.  But if there is an id value, check to make
            # sure there's an actual title associated with it, and if so, create a 
            # new form_t using that title as an instance

            # this part should probably be done in the validate data section of the formset or the InfoForm?
            form_t = TitleForm(data=data_t)
            if data_t.has_key('id') and len(data_t['id']) > 0:
                if len(Lower.Title.objects.filter(id=data_t['id'])) > 0:
                    model_t = Lower.Title.objects.get(pk=data_t['id'])
                    form_t = TitleForm(data=data_t, instance=model_t)

            if form_t.is_valid():
                form_t.save()

            # extract data for desc and process
            data_d = extract_dict(dict_request, 'd')

            # create a generic form_d.  But if there is an id value, check to make
            # sure there's an actual title associated with it, and if so, create a 
            # new form_d using that title as an instance

            # this part should probably be done in the validate data section of the formset or the InfoForm?
            form_d = DescForm(data=data_d)
            if data_d.has_key('id') and len(data_d['id']) > 0:
                if len(Lower.Desc.objects.filter(id=data_d['id'])) > 0:
                    model_d = Lower.Desc.objects.get(pk=data_d['id'])
                    form_d = DescForm(data=data_d, instance=model_d)

            if form_d.is_valid():
                form_d.save()
        """
    else:
        form_lower = LowerForm(instance=m_lower)

    return render_to_response(
                "admin/nested/lower.html",
                {
                    'form_lower':form_lower,
                    'formset_info':formset_info,
                    'type':str(type(id_lower)),
                    'initial': initial_list(id_lower, 1),
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
