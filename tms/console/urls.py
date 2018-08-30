# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    DashboardView,
    TestRunView,
    TestCaseView,
    ReportView,
)
from console.example.example_views import DefaultFormsetView, DefaultFormView, DefaultFormByFieldView, \
    FormHorizontalView, FormInlineView, FormWithFilesView, PaginationView, MiscView
from console.project.project_views import ProjectListView, ProjectCreateView, ProjectView, ProjectUpdateView, \
    ProjectDeleteView
from console.release.release_views import ReleaseCreateView, ReleaseListView, ReleaseUpdateView, ReleaseDeleteView
from console.device.device_views import DeviceCreateView, DeviceListView, DeviceUpdateView, DeviceDeleteView
from console.message.message_views import MessageCreateView, MessageListView, MessageUpdateView, MessageDeleteView
from console.test_case.test_case_views import TestCaseCreateView, TestCaseListView, TestCaseUpdateView, TestCaseDeleteView

app_name = 'console'
urlpatterns = [
    url(r"^$", DashboardView.as_view(), name="home"),
    url(r"^formset$", DefaultFormsetView.as_view(), name="formset_default"),
    url(r"^form$", DefaultFormView.as_view(), name="form_default"),
    url(r"^form_by_field$", DefaultFormByFieldView.as_view(), name="form_by_field"),
    url(r"^form_horizontal$", FormHorizontalView.as_view(), name="form_horizontal"),
    url(r"^form_inline$", FormInlineView.as_view(), name="form_inline"),
    url(r"^form_with_files$", FormWithFilesView.as_view(), name="form_with_files"),
    url(r"^pagination$", PaginationView.as_view(), name="pagination"),
    url(r"^misc$", MiscView.as_view(), name="misc"),

    url(r"^project/(?P<pk>\d+)/$", ProjectView.as_view(), name='overview'),
    url(r"^project/add/$", ProjectCreateView.as_view(), name='project_create'),
    url(r"^project/list/$", ProjectListView.as_view(), name='project_list'),
    url(r"^project/(?P<pk>\d+)/update/$", ProjectUpdateView.as_view(), name='project_update'),
    url(r"^project/(?P<pk>\d+)/delete/$", ProjectDeleteView.as_view(), name='project_delete'),

    url(r"^project/(?P<pk>\d+)/report/$", ReportView.as_view(), name='report'),

    # url(r"^project/(?P<pk>\d+)/release/$", ReleaseView.as_view(), name='release'),
    url(r"^project/(?P<pk>\d+)/release/list/$", ReleaseListView.as_view(), name='release_list'),
    url(r"^project/(?P<pk>\d+)/release/add/$", ReleaseCreateView.as_view(), name='release_add'),
    url(r"^release/(?P<pk>\d+)/update/$", ReleaseUpdateView.as_view(), name='release_update'),
    url(r"^release/(?P<pk>\d+)/delete/$", ReleaseDeleteView.as_view(), name='release_delete'),

    url(r"^device/add/$", DeviceCreateView.as_view(), name='device_create'),
    url(r"^device/list/$", DeviceListView.as_view(), name='device_list'),
    url(r"^device/(?P<pk>\d+)/update/$", DeviceUpdateView.as_view(), name='device_update'),
    url(r"^device/(?P<pk>\d+)/delete/$", DeviceDeleteView.as_view(), name='device_delete'),

    url(r"^message/add/$", MessageCreateView.as_view(), name='message_create'),
    url(r"^message/list/$", MessageListView.as_view(), name='message_list'),
    url(r"^message/(?P<pk>\d+)/update/$", MessageUpdateView.as_view(), name='message_update'),
    url(r"^message/(?P<pk>\d+)/delete/$", MessageDeleteView.as_view(), name='message_delete'),

    # url(r"^test_case/add/$", TestCaseCreateView.as_view(), name='test_case_create'),
    # url(r"^test_case/list/$", TestCaseListView.as_view(), name='test_case_list'),
    # url(r"^test_case/(?P<pk>\d+)/update/$", TestCaseUpdateView.as_view(), name='test_case_update'),
    # url(r"^test_case/(?P<pk>\d+)/delete/$", TestCaseDeleteView.as_view(), name='test_case_delete'),

    url(r"^project/(?P<pk>\d+)/test_run/$", TestRunView.as_view(), name='test_run'),

    # url(r"^project/(?P<pk>\d+)/test_case/$", TestCaseView.as_view(), name='test_case'),
    url(r"^project/(?P<pk>\d+)/test_case/$", TestCaseListView.as_view(), name='test_case_overview'),
    url(r"^project/(?P<pk>\d+)/test_case/add/$", TestCaseCreateView.as_view(), name='test_case_create'),
    url(r"^test_case/(?P<pk>\d+)/update/$", TestCaseUpdateView.as_view(), name='test_case_update'),
    url(r"^test_case/(?P<pk>\d+)/delete/$", TestCaseDeleteView.as_view(), name='test_case_delete'),

]
