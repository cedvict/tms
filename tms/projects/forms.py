# Django
from django import forms
# Local
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['timestamp']
