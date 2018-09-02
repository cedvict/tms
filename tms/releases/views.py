# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Local
from .forms import ReleaseForm
from .models import Release

from news.models import News
from test_runs.models import TestRun

from django.template.defaulttags import register

from django.db.models import Q

from base.base import TEST_RUN_STATUS_ACTIVE, TEST_RUN_STATUS_CREATED, TEST_RUN_STATUS_BLOCKED, \
    RELEASE_STATUS_CREATED, RELEASE_STATUS_ACTIVE


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class Index(generic.ListView):
    model = Release
    context_object_name = 'releases'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        releases = Release.objects.all()
        context['all_release_list'] = releases
        context['last_ten_news_list'] = News.objects.all().order_by('-id')[:5]
        test_run_stats = {}
        for p in releases:
            test_run_stats[p.id] = TestRun.objects.filter(Q(release__id=p.id),
                                                          Q(test_run_status=TEST_RUN_STATUS_CREATED) | Q(
                                                              test_run_status=TEST_RUN_STATUS_ACTIVE) | Q(
                                                              test_run_status=TEST_RUN_STATUS_BLOCKED)).count()
        context['test_run_stats'] = test_run_stats

        context['does_enter_a_release'] = False

        return context


class ReleaseOverviewView(generic.DetailView):
    model = Release
    template_name = 'releases/release_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_release'] = True
        return context


class ReleaseCreateView(generic.CreateView):
    template_name = 'releases/create_release.html'
    form_class = ReleaseForm
    success_url = reverse_lazy('dashboard')


class ReleaseUpdateView(generic.UpdateView):
    model = Release
    template_name = 'releases/update_release.html'
    form_class = ReleaseForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_release'] = True
        return context


class ReleaseReadView(generic.DetailView):
    model = Release
    template_name = 'releases/read_release.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_release'] = True
    #     return context


class ReleaseDetailView(generic.DetailView):
    model = Release
    template_name = 'releases/release_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        release = Release.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['does_enter_a_release'] = True
        context['GLOBAL_PROJECT_ID'] = release.pk
        context['GLOBAL_PROJECT_NAME'] = release.name
        return context


class ReleaseDeleteView(generic.DeleteView):
    model = Release
    template_name = 'releases/delete_release.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_release'] = True
        return context
