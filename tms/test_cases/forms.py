# Django
from django import forms
# Local
from .models import TestCase


class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        exclude = ['timestamp']
