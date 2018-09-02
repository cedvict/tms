# Django
from django import forms
# Local
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['timestamp']
