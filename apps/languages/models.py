from django.db import models


class LanguageChoice(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=6)
    menu_order = models.IntegerField(help_text="this determines how the choice for language will be displayed in menus")
    is_activated = models.BooleanField(help_text="are we using this language?")

    def __unicode__(self):
        return "[%s] %s" % (self.code, self.name)

def get_default_LanguageChoice():
    langs = LanguageChoice.objects.filter(is_activated=True)
    if len(langs) > 0:
        return langs[0].id
    
    return None

class ATextField(models.Model):
    language_choice = models.ForeignKey(LanguageChoice)
    text = models.TextField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s" % self.text

class ACharField(models.Model):
    language_choice = models.ForeignKey(LanguageChoice)
    text = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __unicode__(self):

        return "%s" % self.text

class ATitleDesc(models.Model):
    language_choice = models.ForeignKey(LanguageChoice, default=get_default_LanguageChoice(), limit_choices_to=models.Q(is_activated=True))
    title = models.CharField(max_length=200)
    desc = models.TextField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return "title = %s, desc = %s" % (self.title, self.desc)
