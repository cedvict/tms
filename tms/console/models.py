import datetime

from django.db import models
from django.utils import timezone

PLATFORM_GENERIC = 0
PLATFORM_ANDROID = 1
PLATFORM_IOS = 2
PLATFORM_WEB = 3
PLATFORM_OTHERS = 4
PLATFORM_CHOICES = (
    (PLATFORM_GENERIC, 'Generic'),
    (PLATFORM_ANDROID, 'Android'),
    (PLATFORM_IOS, 'iOS'),
    (PLATFORM_WEB, 'Web'),
    (PLATFORM_OTHERS, 'Others'),
)


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


class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    release_platform = models.IntegerField(choices=PLATFORM_CHOICES, default=PLATFORM_GENERIC)
    release_note = models.CharField(max_length=200)
    RELEASE_STATUS_CREATED = 0
    RELEASE_STATUS_ACTIVE = 1
    RELEASE_STATUS_RELEASED = 2
    RELEASE_STATUS_DISCARDED = 3
    RELEASE_STATUS_CHOICES = (
        (RELEASE_STATUS_CREATED, 'Created'),
        (RELEASE_STATUS_ACTIVE, 'Active'),
        (RELEASE_STATUS_RELEASED, 'Released'),
        (RELEASE_STATUS_DISCARDED, 'Discarded'),
    )
    release_status = models.IntegerField(choices=RELEASE_STATUS_CHOICES, default=RELEASE_STATUS_CREATED)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    def __str__(self):
        return self.project.name + ' ' + self.name + ' ' + str(PLATFORM_CHOICES[self.release_platform][1])

    class Meta:
        db_table = 'release_tab'


class TestPlan(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_plan_tab'


class TestRun(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    test_plan = models.ForeignKey(TestPlan, on_delete=models.DO_NOTHING)

    TEST_RUN_STATUS_CREATED = 0
    TEST_RUN_STATUS_ACTIVE = 1
    TEST_RUN_STATUS_BLOCKED = 2
    TEST_RUN_STATUS_COMPLETED = 3
    TEST_RUN_STATUS_DISCARDED = 4
    TEST_RUN_STATUS_CHOICES = (
        (TEST_RUN_STATUS_CREATED, 'Created'),
        (TEST_RUN_STATUS_ACTIVE, 'Active'),
        (TEST_RUN_STATUS_BLOCKED, 'Blocked'),
        (TEST_RUN_STATUS_COMPLETED, 'Completed'),
        (TEST_RUN_STATUS_DISCARDED, 'Discarded'),
    )

    test_run_status = models.IntegerField(choices=TEST_RUN_STATUS_CHOICES, default=TEST_RUN_STATUS_CREATED)

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

    TEST_CASE_TYPE_FUNCTIONAL = 0
    TEST_CASE_TYPE_ACCEPTANCE = 1
    TEST_CASE_TYPE_ACCESSIBILITY = 2
    TEST_CASE_TYPE_AUTOMATED = 3
    TEST_CASE_TYPE_COMPATIBILITY = 4
    TEST_CASE_TYPE_PERFORMANCE = 5
    TEST_CASE_TYPE_REGRESSION = 6
    TEST_CASE_TYPE_SECURITY = 7
    TEST_CASE_TYPE_SANITY = 8
    TEST_CASE_TYPE_USABILITY = 9
    TEST_CASE_TYPE_LOCALIZATION = 10
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

    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    component = models.ForeignKey(Component, on_delete=models.DO_NOTHING)

    TEST_CASE_TIER_0 = 0
    TEST_CASE_TIER_1 = 1
    TEST_CASE_TIER_2 = 2
    TEST_CASE_TIER_3 = 3
    TEST_CASE_TIER_4 = 4
    TEST_CASE_TIER_CHOICES = (
        (TEST_CASE_TIER_0, 'tier 0'),
        (TEST_CASE_TIER_1, 'tier 1'),
        (TEST_CASE_TIER_2, 'tier 2'),
        (TEST_CASE_TIER_3, 'tier 3'),
        (TEST_CASE_TIER_4, 'tier 4'),
    )

    test_case_tier = models.IntegerField(choices=TEST_CASE_TIER_CHOICES, default=TEST_CASE_TIER_1)

    test_case_platform = models.IntegerField(choices=PLATFORM_CHOICES)
    preconditions = models.CharField(max_length=200)
    test_steps = models.CharField(max_length=2000)
    expected_result = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'test_case_tab'


class TestRunCase(models.Model):
    comment = models.CharField(max_length=500)
    test_run = models.ForeignKey(TestRun, on_delete=models.CASCADE)
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)

    actual_result = models.CharField(max_length=500, default=None, blank=True, null=True)

    TEST_RUN_CASE_STATUS_SUCCEED = 0
    TEST_RUN_CASE_STATUS_FAILED = 1
    TEST_RUN_CASE_STATUS_ERROR = 2
    TEST_RUN_CASE_STATUS_SKIPPED = 3
    TEST_RUN_CASE_STATUS_NOT_STARTED = 4
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


class Message(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', auto_now_add=True, blank=True)
    upd_date = models.DateTimeField('date updated', auto_now=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'message_tab'
