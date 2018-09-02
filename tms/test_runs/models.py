from django.db import models
from simple_history.models import HistoricalRecords

from base.base import TEST_RUN_STATUS_CHOICES, TEST_RUN_STATUS_CREATED, TEST_RUN_CASE_STATUS_CHOICES, \
    TEST_RUN_CASE_STATUS_NOT_STARTED
from projects.models import Project
from django.conf import settings
from test_cases.models import TestCase
from test_plans.models import TestPlan


class TestRun(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    test_plan = models.ForeignKey(TestPlan, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=None, blank=True)
    test_run_status = models.IntegerField(choices=TEST_RUN_STATUS_CHOICES, default=TEST_RUN_STATUS_CREATED)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_run_tab'

    history = HistoricalRecords()


class TestRunCase(models.Model):
    comment = models.CharField(max_length=500)
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    actual_result = models.CharField(max_length=500, default=None, blank=True, null=True)

    test_run_case_status = models.IntegerField(choices=TEST_RUN_CASE_STATUS_CHOICES,
                                               default=TEST_RUN_CASE_STATUS_NOT_STARTED)

    def __str__(self):
        return self.test_run.name + self.test_case.name
