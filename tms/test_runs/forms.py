# Django
from django import forms
# Local
from .models import TestRun


class TestRunForm(forms.ModelForm):
    class Meta:
        model = TestRun
        exclude = ['timestamp']
