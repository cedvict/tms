# Django
from django import forms
# Local
from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ['timestamp']
