# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.db.models.fields.files import FieldFile
from django.views.generic.base import TemplateView

from django.views import generic

from django.db.models import Q

from .models import Project, Message, Release, TestRun

from django.template.defaulttags import register

from console.base.base import TEST_RUN_STATUS_ACTIVE, TEST_RUN_STATUS_CREATED, TEST_RUN_STATUS_BLOCKED, \
    RELEASE_STATUS_CREATED, RELEASE_STATUS_ACTIVE


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, "dummy.txt")


class DashboardView(TemplateView):
    template_name = "console/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['all_project_list'] = projects
        context['last_five_messages_list'] = Message.objects.all().order_by('-id')[:5]

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
        return context


class TestRunView(generic.DetailView):
    model = Project
    template_name = 'console/test_run.html'


class TestCaseView(generic.DetailView):
    model = Project
    template_name = 'console/test_case.html'


class ReportView(generic.DetailView):
    model = Project
    template_name = 'console/report.html'
