from nested.models import Lower
from nested.forms import InfoForm, BaseInfoFormSet
from languages.models import LanguageChoice

langs = LanguageChoice.objects.all()

def dellall(lower):
    Lower.Desc.objects.filter(primary=lower).delete()
    Lower.Title.objects.filter(primary=lower).delete()

def getall(lower):
    return Lower.Title.objects.filter(primary=lower), Lower.Desc.objects.filter(primary=lower)

def initall(lower):
    dellall(lower)
    Lower.Desc(primary=lower, language_choice=langs[0], text="DEBUG_LOWER_DESC_EN").save()
    Lower.Desc(primary=lower, language_choice=langs[1], text="DEBUG_LOWER_DESC_FR").save()

    Lower.Title(primary=lower, language_choice=langs[0], text="DEBUG_LOWER_TITLE_EN").save()
    Lower.Title(primary=lower, language_choice=langs[1], text="DEBUG_LOWER_TITLE_FR").save()




def initial_list1(lower, num=1):

    # make sure lower has an id attribute
    id_lower = u''
    if hasattr(lower, "id"):
        id_lower = lower.id
    elif isinstance(lower, (int, long)):
        id_lower = lower
    elif isinstance(lower, (str, unicode)):
        id_lower = int(lower)
    
    d_initial = {'id_lower': id_lower}

    # return a list of duplicated values for dict_initial
    return [d_initial.copy() for i in range(0, num)]


def pfmst(formset):
    for form in formset.forms:
        print form
        print "\n"

def clean_request(dict_from):
    dict_to = dict()

    for k in dict_from:
        dict_to[k] = dict_from[k][0]

    return dict_to

def test_retrieve(m_lower):

    # initialize the list, if it's nothing don't use it
    l_initial = list()

    if m_lower != None:

        for lang in LanguageChoice.objects.all():
            l_titles = Lower.Title.objects.filter(language_choice=lang).filter(primary=m_lower)
            l_descs = Lower.Desc.objects.filter(language_choice=lang).filter(primary=m_lower)

            d_initial = dict()

            if len(l_titles):
                d_initial['lower_title'] = l_titles[0]
                d_initial['title'] = l_titles[0].text

            if len(l_descs):
                d_initial['lower_desc'] = l_descs[0]
                d_initial['description'] = l_descs[0].text

            # if anything got retrieved then add the rest and append it to the main list
            if len(d_initial):
                d_initial['lower'] = m_lower
                d_initial['language'] = lang
                l_initial.append(d_initial)

        return l_initial


from django.forms.formsets import formset_factory
FSET_Info_0 = formset_factory(InfoForm, extra=0, can_delete=True)
FSET_Info_1 = formset_factory(InfoForm, extra=1, can_delete=True)
FSET_Info_2 = formset_factory(InfoForm, extra=2, can_delete=True)
FSET_Info_3 = formset_factory(InfoForm, extra=3, can_delete=True)



data_list = list()

data_list.append(clean_request({u'image_large': [u''], u'form-0-lower': [u'1'], u'form-0-lower_desc': [u'57'], u'form-1-title': [u''], u'name': [u'LOWER_1'], u'form-1-lower': [u''], u'top': [u'1'], u'form-0-language': [u'1'], u'form-0-desc': [u'fghg'], u'form-TOTAL_FORMS': [u'2'], u'form-0-title': [u'hgfh'], u'form-1-desc': [u''], u'form-1-lower_desc': [u''], u'form-INITIAL_FORMS': [u'1'], u'form-0-lower_title': [u'65'], u'image_thumb': [u''], u'form-1-language': [u''], u'form-0-DELETE': [u'on'], u'_continue': [u'Save and continue editing'], u'form-1-lower_title': [u'']}))

data_list.append(clean_request({u'form-0-lower': [u''], u'form-0-lower_desc': [u''], u'form-1-description': [u''], u'name': [u'debug lower_form 1'], u'form-0-description': [u''], u'form-1-lower': [u''], u'top': [u'1'], u'form-INITIAL_FORMS': [u'0'], u'form-1-lower_desc': [u''], u'form-TOTAL_FORMS': [u'2'], u'form-0-lower_title': [u''], u'form-0-language': [u''], u'form-0-title': [u''], u'form-1-title': [u''], u'form-1-language': [u''], u'_continue': [u'Save and continue editing'], u'form-1-lower_title': [u'']}))

data_list.append(clean_request({u'form-0-lower': [u''], u'form-0-lower_desc': [u''], u'form-1-description': [u''], u'name': [u'debug lower_form 1'], u'form-0-description': [u'DEBUG_LOWER_DESC_EN_NEW'], u'form-1-lower': [u''], u'top': [u'1'], u'form-INITIAL_FORMS': [u'0'], u'form-1-lower_desc': [u''], u'form-TOTAL_FORMS': [u'2'], u'form-0-lower_title': [u''], u'form-0-language': [u'1'], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN_NEW'], u'form-1-title': [u''], u'form-1-language': [u''], u'_continue': [u'Save and continue editing'], u'form-1-lower_title': [u'']}))

data_list.append(clean_request({u'form-0-lower': [u''], u'form-0-lower_desc': [u''], u'form-1-description': [u''], u'name': [u'debug lower_form 1'], u'form-0-description': [u'DEBUG_LOWER_DESC_EN_NEW_1'], u'form-1-lower': [u''], u'top': [u'1'], u'form-INITIAL_FORMS': [u'0'], u'form-1-lower_desc': [u''], u'form-TOTAL_FORMS': [u'2'], u'form-0-lower_title': [u''], u'form-0-language': [u'1'], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN_NEW_1'], u'form-1-title': [u''], u'form-1-language': [u''], u'_continue': [u'Save and continue editing'], u'form-1-lower_title': [u'']}))


data_list.append(clean_request({u'form-0-lower_desc': [u'15'], u'form-0-description': [u'DEBUG_LOWER_DESC_EN'], u'form-1-lower_desc': [u'16'], u'form-2-lower': [u''], u'form-2-lower_desc': [u''], u'form-0-language': [u'1'], u'form-1-title': [u'DEBUG_LOWER_TITLE_FR'], u'_continue': [u'Save and continue editing'], u'form-2-description': [u''], u'top': [u'1'], u'form-0-lower_title': [u'24'], u'form-1-lower_title': [u'25'], u'form-1-description': [u'DEBUG_LOWER_DESC_FR'], u'form-2-lower_title': [u''], u'form-TOTAL_FORMS': [u'3'], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN'], u'form-2-title': [u''], u'form-INITIAL_FORMS': [u'2'], u'form-0-lower': [u'21'], u'name': [u'debug lower_form 1'], u'form-2-language': [u''], u'form-1-lower': [u'21'], u'form-1-language': [u'2']}))

data_list.append(clean_request({u'form-0-lower_desc': [u'25'], u'form-0-description': [u'DEBUG_LOWER_DESC_EN_CHANGE'], u'form-1-lower_desc': [u'30'], u'form-2-lower': [u''], u'form-2-lower_desc': [u''], u'form-0-language': [u'1'], u'form-1-title': [u'DEBUG_LOWER_TITLE_FR'], u'_continue': [u'Save and continue editing'], u'form-2-description': [u''], u'top': [u'1'], u'form-0-lower_title': [u'35'], u'form-1-lower_title': [u'38'], u'form-0-DELETE': [u'on'], u'form-1-description': [u'DEBUG_LOWER_DESC_FR'], u'form-2-lower_title': [u''], u'form-TOTAL_FORMS': [u'3'], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN'], u'form-2-title': [u''], u'form-INITIAL_FORMS': [u'2'], u'form-0-lower': [u'21'], u'name': [u'debug lower_form 1'], u'form-2-language': [u''], u'form-1-lower': [u'21'], u'form-1-language': [u'2']}))


data_list.append(clean_request({u'form-0-lower_desc': [u'39'], u'form-0-description': [u'DEBUG_LOWER_DESC_EN'], u'form-1-lower_desc': [u'40'], u'form-2-lower': [u''], u'form-2-lower_desc': [u''], u'form-0-language': [u'1'], u'form-1-title': [u'DEBUG_LOWER_TITLE_FR'], u'_continue': [u'Save and continue editing'], u'form-2-description': [u''], u'top': [u'1'], u'form-0-lower_title': [u'49'], u'form-1-lower_title': [u'50'], u'form-0-DELETE': [u'on'], u'form-1-description': [u'DEBUG_LOWER_DESC_FR'], u'form-2-lower_title': [u''], u'form-TOTAL_FORMS': [u'3'], u'form-0-title': [u'DEBUG_LOWER_TITLE_EN'], u'form-2-title': [u''], u'form-INITIAL_FORMS': [u'2'], u'form-0-lower': [u'21'], u'name': [u'debug lower_form 1'], u'form-2-language': [u''], u'form-1-lower': [u'21'], u'form-1-language': [u'2']}))


data_list.append(clean_request({u'form-0-lower_desc': [u'45'], u'form-2-title': [u''], u'form-2-lower': [u''], u'form-2-lower_desc': [u''], u'form-1-DELETE': [u'on'], u'form-2-desc': [u''], u'form-0-language': [u'1'], u'form-1-title': [u'sadf'], u'_continue': [u'Save and continue editing'], u'top': [u'1'], u'form-0-lower_title': [u'56'], u'form-2-DELETE': [u'on'], u'form-0-desc': [u'DEBUG_LOWER_DESC_HEb'], u'form-1-lower_title': [u'57'], u'form-2-lower_title': [u''], u'form-TOTAL_FORMS': [u'3'], u'form-0-title': [u'DEBUG_LOWER_TITLE_HEx'], u'form-INITIAL_FORMS': [u'2'], u'form-1-lower_desc': [u'46'], u'form-1-desc': [u'sdf'], u'form-0-lower': [u'21'], u'name': [u'debug lower_form 1'], u'form-2-language': [u''], u'form-1-lower': [u'21'], u'form-1-language': [u'4']}))
