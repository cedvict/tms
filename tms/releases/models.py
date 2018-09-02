from django.db import models
from simple_history.models import HistoricalRecords

from base.base import PLATFORM_CHOICES, PLATFORM_GENERIC, RELEASE_STATUS_CHOICES, RELEASE_STATUS_CREATED
from projects.models import Project


class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    release_platform = models.IntegerField(choices=PLATFORM_CHOICES, default=PLATFORM_GENERIC)
    release_note = models.CharField(max_length=200)

    release_status = models.IntegerField(choices=RELEASE_STATUS_CHOICES, default=RELEASE_STATUS_CREATED)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    def __str__(self):
        return self.project.name + ' ' + self.name + ' ' + str(PLATFORM_CHOICES[self.release_platform][1])

    class Meta:
        db_table = 'release_tab'

    history = HistoricalRecords()