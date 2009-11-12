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


from django import forms
class TLForm(forms.Form):
    from languages.models import LanguageChoice
    language = forms.ModelChoiceField(queryset=LanguageChoice.objects.filter(is_activated=True), empty_label="Choose Lang")
    title = forms.CharField(max_length="200")

    class Meta:
        model = Lower.Title

    def clean(self):
        return self.cleaned_data

    def get_formset(self):
        from django.forms.formsets import formset_factory
        FS = formset_factory(TLForm, extra=2)
        return FS()


from django.forms import BaseModelForm

class LowerForm(forms.ModelForm):
    tlform = TLForm()

    top = forms.ModelChoiceField(queryset=Top.objects.all(), empty_label="Top objects")
    #name = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(LowerForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(max_length=100)

        for k in self.tlform.fields.iterkeys():
            self.fields[k] = self.tlform.fields[k]

    class Meta:
        model = Lower
        fields = ['name', 'top']#, 'language', 'title']

    def clean(self):
        return self.cleaned_data

    def save(self, commit):
        super(LowerForm, self).save(commit)


        
