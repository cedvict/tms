# Django
from django import forms
# Local
from .models import TestPlan


class TestPlanForm(forms.ModelForm):
    class Meta:
        model = TestPlan
        exclude = ['timestamp']
