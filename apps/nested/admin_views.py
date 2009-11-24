from nested.models import *
from languages.models import *

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required

def report(request, lower_id):
    return lower(request, lower_id)

def lower(request, lower_id=None):

    lower_obj = None
    if lower_id != None:
        lower_obj = Lower.objects.get(id=lower_id)
    lowerform = None

    from django.forms.models import modelformset_factory

    #TitleFSet = modelformset_factory(Lower.Title, max_num=3)
    TitleFSet = modelformset_factory(Lower.Title, can_delete=True, formset=BaseTitleFormSet, max_num=3)
    #TitleFSet = formset_factory(TitleForm, max_num=3) 
    formset_title = TitleFSet(queryset=Lower.Title.objects.filter(primary=lower_obj))

    DescFSet = modelformset_factory(Lower.Desc, max_num=3)
    formset_desc = DescFSet(queryset=Lower.Desc.objects.filter(primary=lower_obj))

    title_instances = None

    if request.method == 'POST':
        lowerform = LowerForm(request.POST, instance=lower_obj)
        lowerform.save()

        formset_title = TitleFSet(request.POST)

        # if it's all good then save it and reload
        if formset_title.is_valid():
            formset_title.save()
            formset_title = TitleFSet(queryset=Lower.Title.objects.filter(primary=lower_obj))

        
        #title_instances = formset_title.save(commit=False)

        # check to make sure we aren't saving multiple objects for the same language_choice
        #for title_instance in title_instances:
        #    title_qs = Lower.Title.objects.filter(primary=title_instance.primary).filter(language_choice=title_instance.language_choice)
        #    if title_qs.count() == 0:
        #        title_instance.save()

        #formset_desc = DescFSet(request.POST)
        #formset_desc.is_valid()
        #formset_desc.save()
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

report = staff_member_required(report)
lower = staff_member_required(lower)
