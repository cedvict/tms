# Django
from django.urls import reverse_lazy
from django.views import generic
# Local
from .forms import ProjectForm
from .models import Project


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
