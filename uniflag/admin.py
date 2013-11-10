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



class FlagAdmin(admin.ModelAdmin):
    form = AFlagForm




admin.site.register(Flag, FlagAdmin)