import datetime

from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    upd_date = models.DateTimeField('date updated')

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


class TestPlan(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    upd_date = models.DateTimeField('date updated')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_plan_tab'


class TestRun(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    test_plan = models.ForeignKey(TestPlan, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_run_tab'


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

    TEST_CASE_TYPE_FUNCTIONAL = 1
    TEST_CASE_TYPE_ACCEPTANCE = 2
    TEST_CASE_TYPE_ACCESSIBILITY = 3
    TEST_CASE_TYPE_AUTOMATED = 4
    TEST_CASE_TYPE_COMPATIBILITY = 5
    TEST_CASE_TYPE_PERFORMANCE = 6
    TEST_CASE_TYPE_REGRESSION = 7
    TEST_CASE_TYPE_SECURITY = 8
    TEST_CASE_TYPE_SANITY = 9
    TEST_CASE_TYPE_USABILITY = 10
    TEST_CASE_TYPE_LOCALIZATION = 11
    TEST_CASE_TYPE_CHOICES = (
        (TEST_CASE_TYPE_FUNCTIONAL, 'Functional'),
        (TEST_CASE_TYPE_ACCEPTANCE, 'Acceptance'),
        (TEST_CASE_TYPE_ACCESSIBILITY, 'Accessibility'),
        (TEST_CASE_TYPE_AUTOMATED, 'Automated'),
        (TEST_CASE_TYPE_COMPATIBILITY, 'Compatibility'),
        (TEST_CASE_TYPE_PERFORMANCE, 'Performance'),
        (TEST_CASE_TYPE_REGRESSION, 'Regression'),
        (TEST_CASE_TYPE_SECURITY, 'Security'),
        (TEST_CASE_TYPE_SANITY, 'Sanity'),
        (TEST_CASE_TYPE_USABILITY, 'Usability'),
        (TEST_CASE_TYPE_LOCALIZATION, 'Localization'),

    )
    test_case_type = models.IntegerField(choices=TEST_CASE_TYPE_CHOICES)
    estimate_in_minute = models.DecimalField(max_digits=5, decimal_places=2)

    created_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    component = models.ForeignKey(Component, on_delete=models.DO_NOTHING)

    TEST_CASE_TIER_1 = 1
    TEST_CASE_TIER_2 = 2
    TEST_CASE_TIER_3 = 3
    TEST_CASE_TIER_4 = 4
    TEST_CASE_TIER_5 = 5
    TEST_CASE_TIER_CHOICES = (
        (TEST_CASE_TIER_1, 'tier 1'),
        (TEST_CASE_TIER_2, 'tier 2'),
        (TEST_CASE_TIER_3, 'tier 3'),
        (TEST_CASE_TIER_2, 'tier 4'),
        (TEST_CASE_TIER_3, 'tier 5'),
    )

    test_case_tier = models.IntegerField(choices=TEST_CASE_TIER_CHOICES, default=TEST_CASE_TIER_1)

    TEST_CASE_PLATFORM_GENERIC = 1
    TEST_CASE_PLATFORM_ANDROID = 2
    TEST_CASE_PLATFORM_IOS = 3
    TEST_CASE_PLATFORM_WEB = 4
    TEST_CASE_PLATFORM_OTHERS = 5
    TEST_CASE_PLATFORM_CHOICES = (
        (TEST_CASE_PLATFORM_GENERIC, 'Generic'),
        (TEST_CASE_PLATFORM_ANDROID, 'Android'),
        (TEST_CASE_PLATFORM_IOS, 'iOS'),
        (TEST_CASE_PLATFORM_WEB, 'Web'),
        (TEST_CASE_PLATFORM_OTHERS, 'Others'),
    )
    test_case_platform = models.IntegerField(choices=TEST_CASE_PLATFORM_CHOICES)
    preconditions = models.CharField(max_length=200)
    test_steps = models.CharField(max_length=2000)
    expected_result = models.CharField(max_length=500)
    actual_result = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_case_tab'


class TestRunCase(models.Model):
    comment = models.CharField(max_length=500)
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    TEST_RUN_CASE_STATUS_SUCCEED = 1
    TEST_RUN_CASE_STATUS_FAILED = 2
    TEST_RUN_CASE_STATUS_ERROR = 3
    TEST_RUN_CASE_STATUS_SKIPPED = 4
    TEST_RUN_CASE_STATUS_NOT_STARTED = 5
    TEST_RUN_CASE_STATUS_CHOICES = (
        (TEST_RUN_CASE_STATUS_SUCCEED, 'Succeed'),
        (TEST_RUN_CASE_STATUS_FAILED, 'Failed'),
        (TEST_RUN_CASE_STATUS_ERROR, 'Error'),
        (TEST_RUN_CASE_STATUS_SKIPPED, 'Skipped'),
        (TEST_RUN_CASE_STATUS_NOT_STARTED, '-'),
    )
    test_run_case_status = models.IntegerField(choices=TEST_RUN_CASE_STATUS_CHOICES,
                                               default=TEST_RUN_CASE_STATUS_NOT_STARTED)

    def __str__(self):
        return self.test_case.name


class Role(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'role_tab'


class Tester(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tester_tab'
