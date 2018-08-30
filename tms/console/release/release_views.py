from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from console.models import Release, Project


class ReleaseCreateView(CreateView):
    model = Release
    # success_url = "/release"
    template_name = 'console/release/release_add.html'
    exclude = ('created_date', 'upd_date')
    fields = ('project', 'name', 'release_note', 'release_status', 'release_platform')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context['project'] = Project.objects.get(pk=pk)
        return context

    def get_success_url(self):
        return reverse('console:release_list', kwargs={self.kwargs.get('pk')})


class ReleaseView(generic.DetailView):
    model = Release
    template_name = 'console/release_overview.html'


class ReleaseListView(generic.ListView):
    model = Release
    template_name = 'console/release/release_list.html'
    # paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        project = Project.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['release_list'] = Release.objects.filter(project=project)
        return context


class ReleaseUpdateView(UpdateView):
    model = Release
    fields = ('project', 'name', 'release_note', 'release_status', 'release_platform')
    template_name = 'console/release/release_update.html'

    def get_success_url(self):
        release = Release.objects.get(pk=self.kwargs.get("pk"))
        return reverse('console:release_list', kwargs={'pk': release.project.id})


class ReleaseDeleteView(DeleteView):
    model = Release
    template_name = 'console/release/release_delete.html'

    def get_success_url(self):
        release = Release.objects.get(pk=self.kwargs.get("pk"))
        return reverse('console:release_list', kwargs={'pk': release.project.id})
