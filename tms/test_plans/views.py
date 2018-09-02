# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Local
from .forms import TestPlanForm
from .models import TestPlan

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
    model = TestPlan
    context_object_name = 'test_plans'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_plans = TestPlan.objects.all()
        context['all_test_plan_list'] = test_plans
        context['last_ten_news_list'] = News.objects.all().order_by('-id')[:5]
        test_run_stats = {}
        for p in test_plans:
            test_run_stats[p.id] = TestRun.objects.filter(Q(test_plan__id=p.id),
                                                          Q(test_run_status=TEST_RUN_STATUS_CREATED) | Q(
                                                              test_run_status=TEST_RUN_STATUS_ACTIVE) | Q(
                                                              test_run_status=TEST_RUN_STATUS_BLOCKED)).count()
        context['test_run_stats'] = test_run_stats

        context['does_enter_a_test_plan'] = False

        return context


class TestPlanOverviewView(generic.DetailView):
    model = TestPlan
    template_name = 'test_plans/test_plan_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_test_plan'] = True
        return context


class TestPlanCreateView(generic.CreateView):
    template_name = 'test_plans/create_test_plan.html'
    form_class = TestPlanForm
    success_url = reverse_lazy('dashboard')


class TestPlanUpdateView(generic.UpdateView):
    model = TestPlan
    template_name = 'test_plans/update_test_plan.html'
    form_class = TestPlanForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_test_plan'] = True
        return context


class TestPlanReadView(generic.DetailView):
    model = TestPlan
    template_name = 'test_plans/read_test_plan.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_test_plan'] = True
    #     return context


class TestPlanDetailView(generic.DetailView):
    model = TestPlan
    template_name = 'test_plans/test_plan_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        test_plan = TestPlan.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['does_enter_a_test_plan'] = True
        context['GLOBAL_PROJECT_ID'] = test_plan.pk
        context['GLOBAL_PROJECT_NAME'] = test_plan.name
        return context


class TestPlanDeleteView(generic.DeleteView):
    model = TestPlan
    template_name = 'test_plans/delete_test_plan.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_test_plan'] = True
        return context
