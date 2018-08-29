from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from console.models import Project, TestRun, TestPlan, Release


class ProjectListView(generic.ListView):
    model = Project
    template_name = 'console/project/project_list.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'console/project/project_add.html'
    exclude = ('created_date', 'upd_date')
    fields = ('name', 'description')

    def get_success_url(self):
        return reverse('console:project_list')


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'console/overview.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        project = Project.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['test_run_list'] = TestRun.objects.filter(project=project)
        context['test_run_activity_list'] = TestRun.history.filter(project__id=pk)
        context['test_plan_activity_list'] = TestPlan.history.filter(project__id=pk)
        context['release_activity_list'] = Release.history.filter(project__id=pk)
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    fields = ('name', 'description')
    template_name = 'console/project/project_update.html'

    def get_success_url(self):
        return reverse('console:project_list')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'console/project/project_delete.html'
    success_url = reverse_lazy('console:project_list')