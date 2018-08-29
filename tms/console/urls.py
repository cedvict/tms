# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    HomePageView,
    FormHorizontalView,
    FormInlineView,
    PaginationView,
    FormWithFilesView,
    DefaultFormView,
    MiscView,
    DefaultFormsetView,
    DefaultFormByFieldView,
    ProjectView,
    TestRunView,
    TestCaseView,
    ReportView,
    ReleaseListView,
    ProjectCreateView,
    ProjectListView,
    ProjectUpdateView,
    ReleaseCreateView,
    ReleaseUpdateView,
    ProjectDeleteView,
    ReleaseDeleteView,
)

app_name = 'console'
urlpatterns = [
    url(r"^$", HomePageView.as_view(), name="home"),
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

    url(r"^project/(?P<pk>\d+)/test_run/$", TestRunView.as_view(), name='test_run'),
    url(r"^project/(?P<pk>\d+)/test_case/$", TestCaseView.as_view(), name='test_case'),
    url(r"^project/(?P<pk>\d+)/report/$", ReportView.as_view(), name='report'),

    # url(r"^project/(?P<pk>\d+)/release/$", ReleaseView.as_view(), name='release'),
    url(r"^project/(?P<pk>\d+)/release/list/$", ReleaseListView.as_view(), name='release_list'),
    url(r"^project/(?P<pk>\d+)/release/add/$", ReleaseCreateView.as_view(), name='release_add'),
    url(r"^release/(?P<pk>\d+)/update/$", ReleaseUpdateView.as_view(), name='release_update'),
    url(r"^release/(?P<pk>\d+)/delete/$", ReleaseDeleteView.as_view(), name='release_delete'),
]
