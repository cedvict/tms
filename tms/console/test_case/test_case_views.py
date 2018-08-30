from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from console.models import TestCase, Project


class TestCaseCreateView(CreateView):
    model = TestCase
    template_name = 'console/test_case/test_case_add.html'
    exclude = ('created_date', 'upd_date')
    fields = (
        'project', 'name', 'description', 'test_case_type', 'estimate_in_minute', 'project', 'component',
        'test_case_tier',
        'test_case_platform', 'preconditions', 'test_steps', 'expected_result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context['project'] = Project.objects.get(pk=pk)
        return context

    def get_success_url(self):
        return reverse('console:test_case_overview', kwargs={'pk': self.kwargs.get("pk")})


# class TestCaseView(generic.DetailView):
#     model = TestCase
#     template_name = 'console/release_overview.html'


class TestCaseOverviewView(generic.ListView):
    model = TestCase
    template_name = 'console/test_case.html'
    context_object_name = 'test_case_list'
    paginate_by = 2

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk')
        project = Project.objects.get(pk=pk)
        return TestCase.objects.filter(project=project)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['project'] = Project.objects.get(pk=pk)
        return context

    class Meta:
        ordering = ["-name"]


class TestCaseUpdateView(UpdateView):
    model = TestCase
    exclude = ('created_date', 'upd_date')
    fields = (
        'project', 'name', 'description', 'test_case_type', 'estimate_in_minute', 'project', 'component',
        'test_case_tier',
        'test_case_platform', 'preconditions', 'test_steps', 'expected_result')
    template_name = 'console/test_case/test_case_update.html'

    def get_success_url(self):
        test_case = TestCase.objects.get(pk=self.kwargs.get("pk"))
        return reverse('console:test_case_overview', kwargs={'pk': test_case.project.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_case = TestCase.objects.get(pk=self.kwargs.get("pk"))
        context['project'] = Project.objects.get(pk=test_case.project_id)
        return context


class TestCaseDeleteView(DeleteView):
    model = TestCase
    template_name = 'console/test_case/test_case_delete.html'

    def get_success_url(self):
        test_case = TestCase.objects.get(pk=self.kwargs.get("pk"))
        return reverse('console:test_case_overview', kwargs={'pk': test_case.project.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test_case = TestCase.objects.get(pk=self.kwargs.get("pk"))
        context['project'] = Project.objects.get(pk=test_case.project_id)
        return context

