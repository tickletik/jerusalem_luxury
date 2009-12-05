from django.db import models
from languages.models import *


class Block(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "%s" % self.name

    class Desc_Block(ATextField):
        primary = models.ForeignKey("Block")
        class Meta:
            verbose_name="Description"
            verbose_name_plural="Description"
    Desc=Desc_Block

class Building(models.Model):
    block = models.ForeignKey(Block)
    name = models.CharField(max_length=200)
    

    def __unicode__(self):
        return "Building %s, Block %s" % (name, block.name)
