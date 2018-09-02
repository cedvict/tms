from django.db import models
from simple_history.models import HistoricalRecords

from base.base import DEVICE_PLATFORM, DEVICE_PLATFORM_ANDROID, DEVICE_STATUS_CHOICES, DEVICE_STATUS_AVAILABLE
from django.conf import settings


class Device(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    sn = models.CharField(max_length=20)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=None, blank=True)

    os_version = models.CharField(max_length=10)
    device_platform = models.IntegerField(choices=DEVICE_PLATFORM, default=DEVICE_PLATFORM_ANDROID)

    device_status = models.IntegerField(choices=DEVICE_STATUS_CHOICES, default=DEVICE_STATUS_AVAILABLE)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'device_tab'
