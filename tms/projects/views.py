# Django
from django.urls import reverse_lazy
from django.views import generic
# Local
from .forms import ProjectForm
from .models import Project

from news.models import News
from test_runs.models import TestRun
from releases.models import Release
from devices.models import Device

from django.template.defaulttags import register

from django.db.models import Q

from base.base import TEST_RUN_STATUS_ACTIVE, TEST_RUN_STATUS_CREATED, TEST_RUN_STATUS_BLOCKED, \
    RELEASE_STATUS_CREATED, RELEASE_STATUS_ACTIVE


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


# TODO:
class MyWorkIndex(generic.ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'device_management.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devices = Device.objects.all()
        context['all_devices_list'] = devices
        context['does_enter_a_project'] = True
        return context


class ProjectOverviewView(generic.DetailView):
    model = Project
    template_name = 'projects/project_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = True
        return context


class ProjectCreateView(generic.CreateView):
    template_name = 'projects/create_project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('dashboard')


class ProjectUpdateView(generic.UpdateView):
    model = Project
    template_name = 'projects/update_project.html'
    form_class = ProjectForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = True
        return context


class ProjectReadView(generic.DetailView):
    model = Project
    template_name = 'projects/read_project.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        project = Project.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = True
        context['GLOBAL_PROJECT_ID'] = project.pk
        context['GLOBAL_PROJECT_NAME'] = project.name
        return context


class ProjectDeleteView(generic.DeleteView):
    model = Project
    template_name = 'projects/delete_project.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = True
        return context
