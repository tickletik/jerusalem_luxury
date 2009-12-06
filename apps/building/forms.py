import building.models as models

from django.forms import ModelForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.forms.formsets import DELETION_FIELD_NAME

TenantFormset = inlineformset_factory(models.Building, models.Tenant, fk_name="building", max_num=3)

class BaseBuildingFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        # allow the super class to create the fields as usual
        super(BaseBuildingFormset, self).add_fields(form, index)

        # created the nested formset
        try:
            instance = self.get_queryset()[index]
            pk_value = instance.pk
        except IndexError:
            instance=None
            pk_value = hash(form.prefix)

        # store the formset in the .nested property
        form.nested = [
                TenantFormset(data = self.data, 
                    instance = instance, 
                    prefix = 'TENANTS_%s' % pk_value)] 

    def is_valid(self):
        result = super(BaseBuildingFormset, self).is_valid()

        for form in self.forms:
            if hasattr(form, 'nested'):
                for n in form.nested:
                    # make sure each nested formset is valid as well
                    result = result and n.is_valid()

        return result


    def save_new(self, form, commit=True):
        """Saves and returns a new model instance for the given form."""

        instance = super(BaseBuildingFormset, self).save_new(form, commit=commit)

        # update the form's instance reference
        form.instance = instance

        # update the instance reference on nested forms
        for nested in form.nested:
            nested.instance = instance

            # iterate over the cleaned data of the nested formset and update the foreignkey reference
            for n_cleaned in nested.cleaned_data:
                n_cleaned[nested.fk.name] = instance

        return instance

    def should_delete(self, form):
        """Convenience method for determining if the form's object will
        be deleted; cribbed from BaseModelFormSet.save_existing_objects."""

        if self.can_delete:
            raw_delete_value = form._raw_value(DELETION_FIELD_NAME)
            should_delete = form.fields[DELETION_FIELD_NAME].clean(raw_delete_value)
            return should_delete

        return False

    def save_all(self, commit=True):
        """Save all formsets and along with their nested formsets."""

        # Save without committing (so self.saved_forms is populated)
        # --- We need self.saved_forms so we can go back and access
        # the nested formsets

        objects = self.save(commit=False)

        # save each instance if commit=True
        if commit:
            for o in objects:
                o.save()

        if not commit:
            self.save_m2m()

        # save the nested formsets
        for form in set(self.initial_forms + self.saved_forms):
            if self.should_delete(form): continue

            for nested in form.nested:
                nested.save(commit=commit)

BuildingFormset  = inlineformset_factory(models.Block, models.Building, formset=BaseBuildingFormset, extra=1)


class BlockForm(ModelForm):
    class Meta:
        model = models.Block
