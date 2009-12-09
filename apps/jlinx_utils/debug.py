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


data_list.append(clean_request({u'location_set-TOTAL_FORMS': [u'1'], u'images_set-1-position': [u''], u'location_set-0-floor': [u'1'], u'amenities_set-0-floor_length': [u'23.00'], u'amenities_set-0-bathrooms': [u'4'], u'titledesc_property_set-TOTAL_FORMS': [u'3'], u'IMAGES_TITLE_DESC_1-1-language_choice': [u''], u'images_set-1-image_large': [u''], u'IMAGES_TITLE_DESC_1870287253-2-desc': [u''], u'is_active': [u'on'], u'IMAGES_TITLE_DESC_1-INITIAL_FORMS': [u'1'], u'images_set-1-image_thumb': [u''], u'titledesc_property_set-0-id': [u'3'], u'amenities_set-0-parking': [u'N'], u'images_set-1-name': [u''], u'location_set-0-neighborhood': [u'1'], u'name': [u'PROPERTY_2'], u'location_set-0-street_en': [u'sdf'], u'IMAGES_TITLE_DESC_1870287253-INITIAL_FORMS': [u'0'], u'images_set-0-id': [u'1'], u'location_set-0-id': [u'1'], u'images_set-0-image_large': [u''], u'amenities_set-0-bedrooms': [u'1'], u'images_set-0-name': [u'sadf'], u'images_set-0-image_thumb': [u''], u'titledesc_property_set-1-language_choice': [u'1'], u'IMAGES_TITLE_DESC_1-2-id': [u''], u'IMAGES_TITLE_DESC_1870287253-1-title': [u''], u'titledesc_property_set-2-id': [u''], u'amenities_set-INITIAL_FORMS': [u'1'], u'IMAGES_TITLE_DESC_1870287253-1-id': [u''], u'IMAGES_TITLE_DESC_1870287253-1-desc': [u''], u'IMAGES_TITLE_DESC_1870287253-2-id': [u''], u'amenities_set-0-garden': [u'S'], u'images_set-TOTAL_FORMS': [u'2'], u'amenities_set-0-has_elevator_shabbat': [u'on'], u'images_set-1-id': [u''], u'titledesc_property_set-0-title': [u'DEBUG_TITLE_P_HE'], u'amenities_set-0-balcony': [u'L'], u'amenities_set-TOTAL_FORMS': [u'1'], u'IMAGES_TITLE_DESC_1870287253-2-title': [u''], u'IMAGES_TITLE_DESC_1-1-id': [u''], u'IMAGES_TITLE_DESC_1870287253-0-title': [u''], u'IMAGES_TITLE_DESC_1-2-desc': [u''], u'_continue': [u'Save and continue editing'], u'IMAGES_TITLE_DESC_1-1-desc': [u''], u'IMAGES_TITLE_DESC_1-0-title': [u'asdf'], u'IMAGES_TITLE_DESC_1-2-language_choice': [u''], u'type': [u'4'], u'titledesc_property_set-2-language_choice': [u''], u'location_set-0-zip': [u'123'], u'images_set-INITIAL_FORMS': [u'1'], u'location_set-0-region': [u'1'], u'titledesc_property_set-1-title': [u'DEBUG_TITLE_P_EN'], u'is_available': [u'on'], u'amenities_set-0-conditioning': [u'P'], u'titledesc_property_set-1-desc': [u'DEBUG_DESC_P_EN'], u'IMAGES_TITLE_DESC_1-0-desc': [u'asdf'], u'IMAGES_TITLE_DESC_1-0-id': [u'1'], u'IMAGES_TITLE_DESC_1870287253-1-language_choice': [u''], u'is_rent': [u'on'], u'titledesc_property_set-0-desc': [u'DEBUG_DESC_P_HE'], u'amenities_set-0-id': [u'1'], u'location_set-0-street_he': [u'sdf'], u'images_set-0-position': [u'0'], u'IMAGES_TITLE_DESC_1870287253-0-desc': [u''], u'IMAGES_TITLE_DESC_1870287253-TOTAL_FORMS': [u'3'], u'IMAGES_TITLE_DESC_1-2-title': [u''], u'titledesc_property_set-1-id': [u'4'], u'location_set-0-city': [u'1'], u'amenities_set-0-elevators': [u'1'], u'location_set-0-apartment_number': [u''], u'IMAGES_TITLE_DESC_1-0-language_choice': [u'1'], u'amenities_set-0-heating': [u'N'], u'titledesc_property_set-2-desc': [u''], u'IMAGES_TITLE_DESC_1870287253-0-id': [u''], u'location_set-INITIAL_FORMS': [u'1'], u'titledesc_property_set-0-language_choice': [u'3'], u'IMAGES_TITLE_DESC_1-1-title': [u''], u'titledesc_property_set-INITIAL_FORMS': [u'2'], u'amenities_set-0-floor_width': [u'34.00'], u'amenities_set-0-number_of_floors': [u'3'], u'IMAGES_TITLE_DESC_1870287253-0-language_choice': [u''], u'IMAGES_TITLE_DESC_1870287253-2-language_choice': [u''], u'titledesc_property_set-2-title': [u''], u'IMAGES_TITLE_DESC_1-TOTAL_FORMS': [u'3']}))

data_list.append(clean_request({u'images_set-0-position': [u'0'], u'IMAGES_TITLE_DESC_1-1-language_choice': [u''], u'amenities_set-TOTAL_FORMS': [u'1'], u'location_set-TOTAL_FORMS': [u'1'], u'IMAGES_TITLE_DESC_1870287253-0-desc': [u''], u'images_set-0-name': [u'sadf'], u'IMAGES_TITLE_DESC_1-1-id': [u''], u'images_set-0-image_large': [u''], u'amenities_set-0-bedrooms': [u'3'], u'amenities_set-0-heating': [u'P'], u'location_set-0-street_he': [u'jhgjkhgkjhgjk'], u'type': [u'4'], u'IMAGES_TITLE_DESC_1-2-title': [u''], u'amenities_set-0-bathrooms': [u'2'], u'IMAGES_TITLE_DESC_1-2-desc': [u''], u'images_set-1-name': [u''], u'_continue': [u'Save and continue editing'], u'IMAGES_TITLE_DESC_1870287253-0-language_choice': [u''], u'IMAGES_TITLE_DESC_1-1-desc': [u''], u'titledesc_property_set-TOTAL_FORMS': [u'3'], u'IMAGES_TITLE_DESC_1-0-title': [u'asdf'], u'location_set-0-region': [u'1'], u'location_set-0-city': [u'1'], u'amenities_set-0-elevators': [u'0'], u'location_set-0-apartment_number': [u''], u'location_set-0-zip': [u'123'], u'amenities_set-0-floor_length': [u'23.00'], u'titledesc_property_set-2-desc': [u'DEBUG_DESC_P_EN'], u'images_set-INITIAL_FORMS': [u'1'], u'IMAGES_TITLE_DESC_1870287253-1-id': [u''], u'images_set-1-image_large': [u''], u'titledesc_property_set-1-language_choice': [u'3'], u'IMAGES_TITLE_DESC_1-2-id': [u''], u'IMAGES_TITLE_DESC_1870287253-1-title': [u''], u'titledesc_property_set-2-id': [u''], u'images_set-1-position': [u''], u'IMAGES_TITLE_DESC_1870287253-2-language_choice': [u''], u'IMAGES_TITLE_DESC_1870287253-2-title': [u''], u'IMAGES_TITLE_DESC_1870287253-0-title': [u''], u'amenities_set-0-number_of_floors': [u'1'], u'titledesc_property_set-2-language_choice': [u'1'], u'IMAGES_TITLE_DESC_1870287253-2-desc': [u''], u'titledesc_property_set-1-id': [u'3'], u'amenities_set-INITIAL_FORMS': [u'1'], u'location_set-INITIAL_FORMS': [u'1'], u'amenities_set-0-parking': [u'N'], u'is_active': [u'on'], u'IMAGES_TITLE_DESC_1-INITIAL_FORMS': [u'1'], u'titledesc_property_set-0-language_choice': [u'2'], u'titledesc_property_set-1-title': [u'DEBUG_TITLE_P_HE'], u'images_set-1-image_thumb': [u''], u'titledesc_property_set-0-id': [u'1'], u'IMAGES_TITLE_DESC_1-1-title': [u''], u'titledesc_property_set-2-title': [u'DEBUG_TITLE_P_EN'], u'titledesc_property_set-INITIAL_FORMS': [u'2'], u'titledesc_property_set-1-desc': [u'DEBUG_DESC_P_HE'], u'IMAGES_TITLE_DESC_1-0-desc': [u'asdf'], u'amenities_set-0-floor_width': [u'34.00'], u'IMAGES_TITLE_DESC_1-0-id': [u'1'], u'IMAGES_TITLE_DESC_1870287253-2-id': [u''], u'images_set-1-id': [u''], u'amenities_set-0-garden': [u'N'], u'IMAGES_TITLE_DESC_1-0-language_choice': [u'1'], u'location_set-0-neighborhood': [u'5'], u'titledesc_property_set-0-DELETE': [u'on'], u'name': [u'PROPERTY_2'], u'location_set-0-floor': [u'1'], u'images_set-TOTAL_FORMS': [u'2'], u'is_rent': [u'on'], u'IMAGES_TITLE_DESC_1-2-language_choice': [u''], u'IMAGES_TITLE_DESC_1870287253-0-id': [u''], u'titledesc_property_set-0-desc': [u'DEBUG_DESC_P_FR'], u'IMAGES_TITLE_DESC_1870287253-TOTAL_FORMS': [u'3'], u'IMAGES_TITLE_DESC_1870287253-1-desc': [u''], u'IMAGES_TITLE_DESC_1870287253-1-language_choice': [u''], u'amenities_set-0-conditioning': [u'N'], u'location_set-0-street_en': [u'sdf'], u'IMAGES_TITLE_DESC_1870287253-INITIAL_FORMS': [u'0'], u'is_available': [u'on'], u'images_set-0-id': [u'1'], u'IMAGES_TITLE_DESC_1-TOTAL_FORMS': [u'3'], u'titledesc_property_set-0-title': [u'DEBUG_TITLE_P_FR'], u'amenities_set-0-balcony': [u'N']}))

data_list.append(clean_request({u'building_set-INITIAL_FORMS': [u'1'], u'TENANTS_3-2-language_choice': [u'3'], u'TENANTS_-89763995-0-language_choice': [u''], u'TENANTS_3-INITIAL_FORMS': [u'3'], u'building_set-0-image_thumb': [u''], u'building_set-0-image_large': [u''], u'TENANTS_3-1-language_choice': [u'2'], u'TENANTS_3-0-language_choice': [u'1'], u'_continue': [u'Save and continue editing'], u'building_set-TOTAL_FORMS': [u'2'], u'TENANTS_3-1-id': [u'7'], u'TENANTS_-89763995-1-id': [u''], u'TENANTS_-89763995-2-language_choice': [u''], u'TENANTS_3-2-desc': [u'DEBUG_DESC_HE'], u'TENANTS_-89763995-2-desc': [u''], u'TENANTS_3-2-title': [u'DEBUG_TITLE_HE'], u'TENANTS_-89763995-2-title': [u''], u'TENANTS_-89763995-1-desc': [u''], u'building_set-0-name': [u'BUILDING_TEST_3'], u'TENANTS_-89763995-0-title': [u''], u'TENANTS_3-2-id': [u'8'], u'building_set-0-id': [u'3'], u'TENANTS_-89763995-1-language_choice': [u''], u'TENANTS_3-1-title': [u'DEBUG_TITLE_FR'], u'TENANTS_3-0-id': [u'6'], u'TENANTS_-89763995-INITIAL_FORMS': [u'0'], u'TENANTS_-89763995-2-id': [u''], u'building_set-1-image_large': [u''], u'TENANTS_-89763995-TOTAL_FORMS': [u'3'], u'building_set-1-image_thumb': [u''], u'name': [u'BLOCK_NAME_2'], u'building_set-1-name': [u''], u'TENANTS_-89763995-0-id': [u''], u'TENANTS_-89763995-1-title': [u''], u'building_set-1-id': [u''], u'TENANTS_3-0-desc': [u'DEBUG_DESC_EN'], u'TENANTS_3-TOTAL_FORMS': [u'3'], u'TENANTS_-89763995-0-desc': [u''], u'TENANTS_3-1-desc': [u'DEBUG_DESC_FR'], u'TENANTS_3-0-title': [u'DEBUG_TITLE_EN']}))
