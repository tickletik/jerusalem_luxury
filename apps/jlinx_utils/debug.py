# Create your views here.
def pfmst(formset):
    for form in formset.forms:
        print form
        print "\n"

def clean_request(dict_from):
    dict_to = dict()

    for k in dict_from:
        dict_to[k] = dict_from[k][0]

    return dict_to


def search_prefix(dict_from, prefix):
    dict_to = dict()

    for k in dict_from:
        if k.startswith(prefix):
            dict_to[k] = dict_from[k]

    if len(dict_to) == 0:
        dict_to = None

    return dict_to

data_list = list()

data_list.append(clean_request({u'building_set-INITIAL_FORMS': [u'1'], u'TENANTS_3-2-language_choice': [u'3'], u'TENANTS_-89763995-0-language_choice': [u''], u'TENANTS_3-INITIAL_FORMS': [u'3'], u'building_set-0-image_thumb': [u''], u'building_set-0-image_large': [u''], u'TENANTS_3-1-language_choice': [u'2'], u'TENANTS_3-0-language_choice': [u'1'], u'_continue': [u'Save and continue editing'], u'building_set-TOTAL_FORMS': [u'2'], u'TENANTS_3-1-id': [u'7'], u'TENANTS_-89763995-1-id': [u''], u'TENANTS_-89763995-2-language_choice': [u''], u'TENANTS_3-2-desc': [u'DEBUG_DESC_HE'], u'TENANTS_-89763995-2-desc': [u''], u'TENANTS_3-2-title': [u'DEBUG_TITLE_HE'], u'TENANTS_-89763995-2-title': [u''], u'TENANTS_-89763995-1-desc': [u''], u'building_set-0-name': [u'BUILDING_TEST_3'], u'TENANTS_-89763995-0-title': [u''], u'TENANTS_3-2-id': [u'8'], u'building_set-0-id': [u'3'], u'TENANTS_-89763995-1-language_choice': [u''], u'TENANTS_3-1-title': [u'DEBUG_TITLE_FR'], u'TENANTS_3-0-id': [u'6'], u'TENANTS_-89763995-INITIAL_FORMS': [u'0'], u'TENANTS_-89763995-2-id': [u''], u'building_set-1-image_large': [u''], u'TENANTS_-89763995-TOTAL_FORMS': [u'3'], u'building_set-1-image_thumb': [u''], u'name': [u'BLOCK_NAME_2'], u'building_set-1-name': [u''], u'TENANTS_-89763995-0-id': [u''], u'TENANTS_-89763995-1-title': [u''], u'building_set-1-id': [u''], u'TENANTS_3-0-desc': [u'DEBUG_DESC_EN'], u'TENANTS_3-TOTAL_FORMS': [u'3'], u'TENANTS_-89763995-0-desc': [u''], u'TENANTS_3-1-desc': [u'DEBUG_DESC_FR'], u'TENANTS_3-0-title': [u'DEBUG_TITLE_EN']}))
