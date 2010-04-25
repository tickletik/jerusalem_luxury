from languages.models import *
from nested.models import *

langs = LanguageChoice.objects.all()
lowers = Lower.objects.all()

title = Lower.Title(language_choice=lanchoices[0], primary=lowers[0], text="blah blah blah")
title1 = title
title1.save()


title = Lower.Title(language_choice=lanchoices[2], primary=lowers[0], text="this is in hebrew")
title2 = title
title2.save()

title2 = Lower.Title.objects.filter(primary=lowers[0]).filter(language_choice=lanchoices[2])
title2 = title2[0]     # note this is a queryset list like object

title2.language_choice.name
title2.text
title2.text = "blah blah no really, it's French!"
title2.language_chocie = langs[1]
title2.save()

# django admin doesn't do a good job of showing the correct values when the page is reloaded.  So you might have to go out and back in
