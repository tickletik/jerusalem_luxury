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


def create_initial(fset, lower, num=None):

    # make sure lower has an id attribute
    id_lower = u''
    if hasattr(lower, "id"):
        id_lower = str(lower.id)
    elif isinstance(lower, (int, long)):
        id_lower = str(lower)
    
    return create_initial_list(fset, {'id_lower': id_lower}, num)

def create_initial_list(fset, dict_initial, num=None):

    if num == None:
        extra = fset.extra
        max_num = fset.max_num

        if max_num != 0 and (extra+1) > max_num:
            num = max_num
        else:
            num = extra + 1

    # return a list of duplicated values for dict_initial
    return [dict_initial.copy() for i in range(0, num)]
            


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
FSET_Info_3 = formset_factory(InfoForm, extra=3)


data_list = list()
data_list.append({u'form-2-title': [u'DEBUG_LOWER_TITLE_HE'], u'form-1-id_lower': [u''], u'form-0-description': [u'DEBUG_LOWER_DESC_EN'], u'form-2-id_title': [u''], u'form-3-title': [u''], u'form-0-language': [u'1'], u'form-1-title': [u'DEBUG_LOWER_TITLE_FR'], u'form-2-description': [u'DEBUG_LOWER_DESC_HE'], u'form-3-id_title': [u''], u'form-3-language': [u''], u'form-3-description': [u''], u'top': [u'1'], u'form-0-id_desc': [u''], u'form-0-id_lower': [u'21'], u'form-2-id_lower': [u''], u'form-3-id_lower': [u''], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN'], u'form-3-id_desc': [u''], u'form-1-id_title': [u''], u'form-1-description': [u'DEBUG_LOWER_DESC_FR'], u'form-TOTAL_FORMS': [u'4'], u'form-1-id_desc': [u''], u'form-INITIAL_FORMS': [u'1'], u'name': [u'debug lower_form 1'], u'form-2-language': [u'3'], u'form-2-id_desc': [u''], u'form-0-id_title': [u''], u'form-1-language': [u'2']})

data_list.append({u'form-2-title': [u'DEBUG_LOWER_TITLE_HE'], u'form-1-id_lower': [u''], u'form-0-description': [u'DEBUG_LOWER_DESC_EN_1'], u'form-2-id_title': [u''], u'form-3-title': [u''], u'form-0-language': [u'1'], u'form-1-title': [u'DEBUG_LOWER_TITLE_EN_2'], u'form-2-description': [u'DEBUG_LOWER_DESC_HE'], u'form-3-id_title': [u''], u'form-3-language': [u''], u'form-3-description': [u''], u'top': [u'1'], u'form-0-id_desc': [u''], u'form-0-id_lower': [u'21'], u'form-2-id_lower': [u''], u'form-3-id_lower': [u''], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN_1'], u'form-3-id_desc': [u''], u'form-1-id_title': [u''], u'form-1-description': [u'DEBUG_LOWER_DESC_EN_2'], u'form-TOTAL_FORMS': [u'4'], u'form-1-id_desc': [u''], u'form-INITIAL_FORMS': [u'1'], u'name': [u'debug lower_form 1'], u'form-2-language': [u'3'], u'form-2-id_desc': [u''], u'form-0-id_title': [u''], u'form-1-language': [u'1']})


data_list.append({u'form-1-id_desc': [u''], u'form-1-id_title': [u''], u'form-1-description': [u''], u'name': [u'debug lower_form 1'], u'form-0-description': [u'DEBUG_LOWER_TITLE_ID_1'], u'top': [u'1'], u'form-INITIAL_FORMS': [u'1'], u'form-0-id_desc': [u'1'], u'form-TOTAL_FORMS': [u'2'], u'form-0-id_lower': [u'21'], u'form-1-id_lower': [u''], u'form-0-id_title': [u'4'], u'form-0-language': [u'1'], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN_ID_4'], u'form-1-title': [u''], u'form-1-language': [u'']})

data_list.append({u'form-1-id_desc': [u''], u'form-1-id_title': [u''], u'form-1-description': [u'DEBUG_LOWER_DESC_NEW_HE'], u'name': [u'debug lower_form 1'], u'form-0-description': [u'DEBUG_LOWER_TITLE_ID_1'], u'top': [u'1'], u'form-INITIAL_FORMS': [u'1'], u'form-0-id_desc': [u'1'], u'form-TOTAL_FORMS': [u'2'], u'form-0-id_lower': [u'21'], u'form-1-id_lower': [u''], u'form-0-id_title': [u'4'], u'form-0-language': [u'1'], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN_ID_4'], u'form-1-title': [u'DEBUG_LOWER_TITLE_NEW_HE'], u'form-1-language': [u'3']})




