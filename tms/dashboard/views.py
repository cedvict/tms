from django.db.models import Q
from django.template.defaulttags import register
from django.views import generic

from base.base import TEST_RUN_STATUS_COMPLETED, TEST_RUN_STATUS_CREATED, TEST_RUN_STATUS_ACTIVE, \
    TEST_RUN_STATUS_BLOCKED, RELEASE_STATUS_CREATED, \
    RELEASE_STATUS_ACTIVE
from devices.models import Device
from news.models import News
from projects.models import Project
from releases.models import Release
from test_runs.models import TestRun
from weekly_reports.models import WeeklyReport
from datetime import date, timedelta


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class Index(generic.ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['all_project_list'] = projects
        context['last_ten_news_list'] = News.objects.all().order_by('-id')[:5]
        test_run_stats = {}
        for p in projects:
            test_run_stats[p.id] = TestRun.objects.filter(Q(project__id=p.id),
                                                          Q(test_run_status=TEST_RUN_STATUS_CREATED) | Q(
                                                              test_run_status=TEST_RUN_STATUS_ACTIVE) | Q(
                                                              test_run_status=TEST_RUN_STATUS_BLOCKED)).count()
        context['test_run_stats'] = test_run_stats
        release_stats = {}
        for p in projects:
            release_stats[p.id] = Release.objects.filter(Q(project__id=p.id),
                                                         Q(release_status=RELEASE_STATUS_CREATED) | Q(
                                                             release_status=RELEASE_STATUS_ACTIVE)).count()
        context['release_stats'] = release_stats

        context['does_enter_a_project'] = False

        return context


class MyWorkView(generic.ListView):
    model = TestRun
    template_name = 'my_work/my_work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['current_user_id'] = current_user.id

        context['my_weekly_reports'] = WeeklyReport.objects.filter(Q(user__id=current_user.id))

        context['my_uncompleted_test_runs'] = TestRun.objects.filter(Q(user__id=current_user.id),
                                                                     Q(test_run_status=TEST_RUN_STATUS_CREATED) | Q(
                                                                         test_run_status=TEST_RUN_STATUS_ACTIVE) | Q(
                                                                         test_run_status=TEST_RUN_STATUS_BLOCKED)
                                                                     )
        start_date = date.today()
        end_date = start_date + timedelta(days=7)

        context['my_completed_in_7_days_test_runs'] = TestRun.objects.filter(Q(user__id=current_user.id),
                                                                             Q(
                                                                                 test_run_status=TEST_RUN_STATUS_COMPLETED)
                                                                             )
        context['does_enter_a_project'] = False
        return context
