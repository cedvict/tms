import datetime

from django.db import models
from django.utils import timezone

from simple_history.models import HistoricalRecords

from console.base.base import PLATFORM_GENERIC, PLATFORM_CHOICES, TEST_RUN_STATUS_CREATED, TEST_RUN_STATUS_CHOICES, \
    TEST_CASE_TYPE_CHOICES, TEST_CASE_TIER_1, TEST_CASE_TIER_CHOICES, RELEASE_STATUS_CREATED, RELEASE_STATUS_CHOICES, \
    TEST_PLAN_STATUS_CREATED, TEST_PLAN_STATUS_CHOICES, TEST_RUN_CASE_STATUS_NOT_STARTED, TEST_RUN_CASE_STATUS_CHOICES, \
    DEVICE_PLATFORM_ANDROID, DEVICE_PLATFORM, DEVICE_STATUS_AVAILABLE, DEVICE_STATUS_CHOICES


class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pub_date = None

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        db_table = 'project_tab'


class User(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_tab'


class Role(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role_tab'


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + ':' + self.role.name

    class Meta:
        db_table = 'user_role_tab'


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


class TestPlan(models.Model):
    name = models.CharField(max_length=20)
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


class TestRun(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    test_plan = models.ForeignKey(TestPlan, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=True)

    test_run_status = models.IntegerField(choices=TEST_RUN_STATUS_CHOICES, default=TEST_RUN_STATUS_CREATED)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_run_tab'

    history = HistoricalRecords()


class Component(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'component_tab'


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


class TestRunCase(models.Model):
    comment = models.CharField(max_length=500)
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    actual_result = models.CharField(max_length=500, default=None, blank=True, null=True)

    test_run_case_status = models.IntegerField(choices=TEST_RUN_CASE_STATUS_CHOICES,
                                               default=TEST_RUN_CASE_STATUS_NOT_STARTED)

    def __str__(self):
        return self.test_case.name


class Message(models.Model):
    detail = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    def __str__(self):
        return self.detail

    class Meta:
        db_table = 'message_tab'


class Device(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, default=None)

    os_version = models.CharField(max_length=10)
    device_platform = models.IntegerField(choices=DEVICE_PLATFORM, default=DEVICE_PLATFORM_ANDROID)

    device_status = models.IntegerField(choices=DEVICE_STATUS_CHOICES, default=DEVICE_STATUS_AVAILABLE)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'device_tab'
