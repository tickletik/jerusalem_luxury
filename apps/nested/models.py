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

class DescForm(forms.ModelForm):
    class Meta:
        model = Lower.Desc
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


    lower = forms.ModelChoiceField(queryset=Lower.objects.all(), widget=forms.HiddenInput, required=False)
    lower_desc = forms.ModelChoiceField(queryset=Lower.Desc.objects.all(), widget=forms.HiddenInput, required=False)
    lower_title = forms.ModelChoiceField(queryset=Lower.Title.objects.all(), widget=forms.HiddenInput, required=False)





from django.forms.formsets import BaseFormSet
class BaseInfoFormSet(BaseFormSet):
    def testit(self):
        print 'hi'



def initial_list(m_lower):
    # initialize the list, if it's nothing don't use it
    l_initial = list()

    if m_lower != None:

        for lang in LanguageChoice.objects.all():
            l_titles = Lower.Title.objects.filter(language_choice=lang).filter(primary=m_lower)
            l_descs = Lower.Desc.objects.filter(language_choice=lang).filter(primary=m_lower)

            d_initial = dict()

            if len(l_titles):
                d_initial['lower_title'] = l_titles[0].id
                d_initial['title'] = l_titles[0].text

            if len(l_descs):
                d_initial['lower_desc'] = l_descs[0].id
                d_initial['description'] = l_descs[0].text

            # if anything got retrieved then add the rest and append it to the main list
            if len(d_initial):
                d_initial['lower'] = m_lower.id
                d_initial['language'] = lang.id
                l_initial.append(d_initial)

        return l_initial




# NOTE: make sure to use the correct type for FSET!
def initialize_formset(FSET, l_initial):

        formset = FSET(initial=l_initial)

        # set the id_lower attribute to the correct value for all extra fields
        for i in range(formset.initial_form_count(), formset.total_form_count()):
            for k in l_initial[0].keys(): 
                formset.forms[i].fields[k].initial = l_initial[0][k]

        return formset



def transfer_dict(dict_from, prefix):
    dict_to = dict()
    for k in dict_from:
        if k.startswith(prefix):
            dict_to[k[len(prefix)+1:]] = dict_from[k]
    
    return dict_to

def extract_dict(dict_from, type):
    dict_to = dict()
    dict_to['language_choice'] = dict_from['language'].id
    dict_to['primary'] = dict_from['lower'].id

    if type == 't':
        dict_to['text'] = dict_from['title']
    elif type == 'd':
        dict_to['text'] = dict_from['description']

    return dict_to


