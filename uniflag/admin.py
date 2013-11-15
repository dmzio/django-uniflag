from django.contrib import admin
from django import forms
from uniflag.models import Flag

from uniflag import conf


class AFlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        widgets = {
            'value': forms.Select,
        }

    def __init__(self, *args, **kwargs):
        super(AFlagForm, self).__init__(*args, **kwargs)
        current_type = self.instance.flag_type
        print current_type
        self.fields['value'].choices = conf.UNIFLAG_TYPES[current_type]['values']


from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


class FlagValsListFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Flag values')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'flag_value'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        qs = model_admin.queryset(request)
        return ((val, dict(Flag.ALL_VALUES)[val]) for val in set(qs.values_list('value', flat=True)))

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(value__exact=self.value())
        else:
            return queryset


class FlagAdmin(admin.ModelAdmin):
    form = AFlagForm
    list_display = ('__unicode__', 'comment')
    list_filter = ('flag_type', FlagValsListFilter)




admin.site.register(Flag, FlagAdmin)