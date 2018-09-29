from django.db import models
from simple_history.models import HistoricalRecords

from django.conf import settings

from djrichtextfield.models import RichTextField


class WeeklyReport(models.Model):
    name = models.CharField(max_length=50)
    current_task_list = models.CharField(max_length=500)
    created_bug_list = models.CharField(max_length=500)
    followed_up_bug_list = models.CharField(max_length=500)
    todo_task_list = models.CharField(max_length=500)
    good_thing = models.CharField(max_length=500)
    bad_thing = models.CharField(max_length=500)

    content = RichTextField(max_length=500)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=None, blank=True)

    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'weekly_report_tab'
