from django.db import models

from languages.models import ACharField, ATextField


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

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

from django.forms.models import BaseModelFormSet 
class BaseTitleFormSet(BaseModelFormSet):
    #def __init__(self, *args, **kwargs):
    #    self.queryset = Lower.Title.objects.filter(primary=lower)
    #    super(BaseTitleFormSet, self).__init__(*args, **kwargs)

    def clean(self):
        if any(self.errors):
            return
        langs = []
        x = self.total_form_count()
        for i in range(0, self.total_form_count()):
            form = self.forms[i]

            if form.cleaned_data.has_key('language_choice'):
                lang_choice = form.cleaned_data['language_choice']
                if lang_choice in langs:
                    raise forms.ValidationError, "Titles muse have distinct language choices"
                langs.append(lang_choice)
            elif form.cleaned_data.has_key('text'):
                raise forms.ValidationError, "Text must be accompanied by a language"

class LowerForm(forms.ModelForm):
    #name = forms.CharField(max_length=100)
    #title = forms.CharField(max_length=100)
    
    # make sure that values for top fall within acceptable range
    # is_valid will check to see if the value is outside bounds
    class Meta:
        model = Lower
        fields = ['name', 'title', 'description', 'top']

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    #def save(self, commit=True):
        # create new model
    #    lower = ModelForm.save(self, False)
    #    lower.description = self.cleaned_data['description']
    #    lower.save()
    #    return ModelForm.save(self,commit)
        
        
