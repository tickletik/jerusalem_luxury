from django.db import models

from languages.models import ACharField, ATextField, LanguageChoice


# form imports
from django.forms import ModelForm
from django import forms

# Create your models here.
class Top(models.Model):

    def __unicode__(self):
        return "%s" % self.name

    name = models.CharField(max_length=200)


class Lower(models.Model):
    
    def __unicode__(self):
        return "%s" % self.name

    class Desc_Lower(ATextField):
        primary = models.ForeignKey("Lower")
        class Meta:
            verbose_name="Description"
            verbose_name_plural="Description"
    Desc=Desc_Lower

    class Title_Lower(ACharField):
        primary = models.ForeignKey("Lower")
        class Meta:
            verbose_name="Title"
            verbose_name_plural="Title"
    Title=Title_Lower

    top = models.ForeignKey("Top")
    name = models.CharField(max_length="200")
    title = models.CharField(max_length="200")
    description = models.TextField()

class TitleForm(forms.ModelForm):
    class Meta:
        model = Lower.Title
        fields = ['primary', 'language_choice', 'text']


from django.forms.models import BaseModelFormSet 
class BaseTitleFormSet(BaseModelFormSet):
    #def __init__(self, *args, **kwargs):
    #    self.queryset = Lower.Title.objects.filter(primary=lower)
    #    super(BaseTitleFormSet, self).__init__(*args, **kwargs)

    def clean(self):
        if any(self.errors):
            return
        langs = []
        x = 0
        y= 0
        for i in range(0, self.total_form_count()):
            x = self.total_form_count()
            y = i
            form = self.forms[i]

            if form.cleaned_data.has_key('language_choice'):
                lang_choice = form.cleaned_data['language_choice']
                if lang_choice in langs:
                    raise forms.ValidationError, "Titles must have distinct language choices"
                langs.append(lang_choice)
            elif form.cleaned_data.has_key('text'):
                raise forms.ValidationError, "Text must be accompanied by a language"
        return self.cleaned_data

class LowerForm(forms.ModelForm):
    
    # make sure that values for top fall within acceptable range
    # is_valid will check to see if the value is outside bounds
    class Meta:
        model = Lower
        fields = ['name', 'top']

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    #def save(self, commit=True):
        # create new model
    #    lower = ModelForm.save(self, False)
    #    lower.description = self.cleaned_data['description']
    #    lower.save()
    #    return ModelForm.save(self,commit)
        
class InfoForm(forms.Form):
    language = forms.ModelChoiceField(queryset=LanguageChoice.objects.all())
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500, widget=forms.Textarea())


    id_lower = forms.IntegerField(widget=forms.HiddenInput)
    id_title = forms.IntegerField(widget=forms.HiddenInput, required=False)
    id_desc = forms.IntegerField(widget=forms.HiddenInput, required=False)

    def changed_forms(self, formset):
        if formset.form != InfoForm:
            raise Exception("You are using a formset.form = " + str(formset.form) + ", where you should be using one of InfoForm")




# NOTE: make sure to use the correct type for FSET!
def initialize_formset(FSET, l_initial):

        formset = FSET(initial=l_initial)

        # set the id_lower attribute to the correct value for all extra fields
        for i in range(formset.initial_form_count(), formset.total_form_count()):
            for k in l_initial[0].keys(): 
                formset.forms[i].fields[k].initial = l_initial[0][k]

        return formset


def initial_list(lower, num=1):

    # make sure lower has an id attribute
    id_lower = u''
    if hasattr(lower, "id"):
        id_lower = lower.id
    elif isinstance(lower, (int, long)):
        id_lower = lower
    elif isinstance(lower, (str, unicode)):
        id_lower = int(lower)
    
    d_initial = {'id_lower': id_lower}

    # return a list of duplicated values for dict_initial
    return [d_initial.copy() for i in range(0, num)]



def clean_request(dict_from):
    dict_to = dict()

    for k in dict_from:
        dict_to[k] = dict_from[k][0]

    return dict_to

def transfer_dict(dict_from, prefix):
    dict_to = dict()
    for k in dict_from:
        if k.startswith(prefix):
            dict_to[k[len(prefix)+1:]] = dict_from[k]
    
    return dict_to

def extract_dict(dict_from, type):
    dict_to = dict()
    dict_to['language_choice'] = dict_from['language']
    dict_to['primary'] = dict_from['id_lower']

    if type == 't':
        if len(dict_from['id_title']) > 0:
            dict_to['id'] = dict_from['id_title']

        dict_to['text'] = dict_from['title']
    elif type == 'd':
        if len(dict_from['id_desc']) > 0:
            dict_to['id'] = dict_from['id_desc']

        dict_to['text'] = dict_from['desc']

    return dict_to

from django.forms.formsets import formset_factory
FSET_Info_0 = formset_factory(InfoForm, extra=0)
FSET_Info_1 = formset_factory(InfoForm, extra=1)
FSET_Info_2 = formset_factory(InfoForm, extra=2)
FSET_Info_3 = formset_factory(InfoForm, extra=3)


