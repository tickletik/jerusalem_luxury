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
        
        
