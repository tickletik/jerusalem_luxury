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


class LowerForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    lanchoice = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Lower
        fields = ['name']
    def clean(self):
        self.cleaned_data['description'] = self.cleaned_data['lanchoice']
        del self.cleaned_data['lanchoice']
        return self.cleaned_data

    def save(self, commit=True):
        lower = ModelForm.save(self, False)
        lower.description = self.cleaned_data['description']
        lower.save()
        return ModelForm.save(self,commit)
        
        
