# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Local
from .forms import TestCaseForm
from .models import TestCase

from news.models import News


class Index(generic.ListView):
    model = TestCase
    context_object_name = 'test_cases'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_cases = TestCase.objects.all()
        context['all_test_case_list'] = test_cases
        context['last_ten_news_list'] = News.objects.all().order_by('-id')[:5]

        # context['does_enter_a_project'] = False

        return context


class TestCaseOverviewView(generic.ListView):
    model = TestCase
    context_object_name = 'test_cases'
    template_name = 'test_cases/test_case_overview.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context


class TestCaseCreateView(generic.CreateView):
    template_name = 'test_cases/create_test_case.html'
    form_class = TestCaseForm
    success_url = reverse_lazy('test_case_overview')


class TestCaseUpdateView(generic.UpdateView):
    model = TestCase
    template_name = 'test_cases/update_test_case.html'
    form_class = TestCaseForm
    success_url = reverse_lazy('test_cases_overview')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context


class TestCaseReadView(generic.DetailView):
    model = TestCase
    template_name = 'test_cases/read_test_case.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context


class TestCaseDeleteView(generic.DeleteView):
    model = TestCase
    template_name = 'test_cases/delete_test_case.html'
    success_url = reverse_lazy('test_case_overview')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_project'] = True
    #     return context
