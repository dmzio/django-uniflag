from django import forms
from django.core.exceptions import ValidationError
from uniflag.models import Flag


class FlagForm(forms.ModelForm):
    class Meta:
        model = Flag
        exclude = ('user', 'when_added', 'moderator')

    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        exclude.remove('user')  # allow checking against the missing attribute

        try:
            self.instance.validate_unique(exclude=exclude)
        except ValidationError, e:
            self._update_errors(e.message_dict)