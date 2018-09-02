# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Local
from .forms import TestRunForm
from .models import TestRun

from news.models import News


class Index(generic.ListView):
    model = TestRun
    context_object_name = 'test_runs'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_runs = TestRun.objects.all()
        context['all_test_run_list'] = test_runs
        context['last_ten_news_list'] = News.objects.all().order_by('-id')[:5]

        # context['does_enter_a_project'] = False

        return context


class TestRunOverviewView(generic.ListView):
    model = TestRun
    context_object_name = 'test_runs'
    template_name = 'test_runs/test_run_overview.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context


class TestRunCreateView(generic.CreateView):
    template_name = 'test_runs/create_test_run.html'
    form_class = TestRunForm
    success_url = reverse_lazy('test_run_overview')


class TestRunUpdateView(generic.UpdateView):
    model = TestRun
    template_name = 'test_runs/update_test_run.html'
    form_class = TestRunForm
    success_url = reverse_lazy('test_runs_overview')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context


class TestRunReadView(generic.DetailView):
    model = TestRun
    template_name = 'test_runs/read_test_run.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context


class TestRunDeleteView(generic.DeleteView):
    model = TestRun
    template_name = 'test_runs/delete_test_run.html'
    success_url = reverse_lazy('test_run_overview')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context
