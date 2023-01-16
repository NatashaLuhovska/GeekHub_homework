from django import forms

from .models import AddId


class AddIdForm(forms.ModelForm):

    class Meta:
        model = AddId
        fields = ('string_ids',)
