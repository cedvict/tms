# Django
from django import forms
# Local
from .models import WeeklyReport


class WeeklyReportForm(forms.ModelForm):
    class Meta:
        model = WeeklyReport
        exclude = ['timestamp']
