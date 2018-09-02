from django.db import models
from simple_history.models import HistoricalRecords

from base.base import TEST_PLAN_STATUS_CHOICES, TEST_PLAN_STATUS_CREATED
from projects.models import Project


class TestPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_plan_tab'

    history = HistoricalRecords()

    test_plan_status = models.IntegerField(choices=TEST_PLAN_STATUS_CHOICES, default=TEST_PLAN_STATUS_CREATED)