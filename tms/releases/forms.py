# Django
from django import forms
# Local
from .models import Release


class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        exclude = ['timestamp']
