from django.db import models
from simple_history.models import HistoricalRecords

from base.base import TEST_CASE_TYPE_CHOICES, TEST_CASE_TIER_CHOICES, TEST_CASE_TIER_1, PLATFORM_CHOICES
from projects.models import Project, Component


class TestCase(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    test_case_type = models.IntegerField(choices=TEST_CASE_TYPE_CHOICES)
    estimate_in_minute = models.DecimalField(max_digits=5, decimal_places=2)

    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    component = models.ForeignKey(Component, on_delete=models.DO_NOTHING)

    test_case_tier = models.IntegerField(choices=TEST_CASE_TIER_CHOICES, default=TEST_CASE_TIER_1)

    test_case_platform = models.IntegerField(choices=PLATFORM_CHOICES)
    preconditions = models.CharField(max_length=200)
    test_steps = models.CharField(max_length=2000)
    expected_result = models.CharField(max_length=500)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_case_tab'
