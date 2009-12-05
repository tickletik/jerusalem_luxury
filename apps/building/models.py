from django.db import models
from languages.models import *


class Block(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.name

class Building(models.Model):
    block = models.ForeignKey(Block)
    name = models.CharField(max_length=200)
    image_large = models.ImageField(upload_to="img/nested/large")
    image_thumb = models.ImageField(upload_to="img/nested/thumb")
    
    def __unicode__(self):
        return "Building %s, Block %s" % (name, block.name)

class Tenant(models.Model):
    building = models.ForeignKey(Building)

    language_choice = models.ForeignKey(LanguageChoice)
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __unicode(self):
        return "title = %s, desc = %s, language = %s" % (self.title, self.desc, self.language_choice.name)
