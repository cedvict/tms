from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from console.models import TestCase, Project


class TestCaseCreateView(CreateView):
    model = TestCase
    success_url = "/release"
    template_name = 'console/release/release_add.html'
    exclude = ('created_date', 'upd_date')
    fields = ('project', 'name', 'release_note', 'release_status', 'release_platform')

    def get_success_url(self):
        return reverse('console:release_list', kwargs={'pk': self.kwargs.get("pk")})


class TestCaseView(generic.DetailView):
    model = TestCase
    template_name = 'console/release_overview.html'


class TestCaseListView(generic.ListView):
    model = TestCase  # shorthand for setting queryset = models.Car.objects.all()
    template_name = 'console/test_case/test_case_list.html'  # optional (the default is app_name/modelNameInLowerCase_list.html; which will look into your templates folder for that path and file)
    context_object_name = "test_case_list"  # default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 2

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get("pk")
        project = Project.objects.get(pk=pk)
        return TestCase.objects.filter(project=project)


class TestCaseUpdateView(UpdateView):
    model = TestCase
    fields = ('project', 'name', 'release_note', 'release_status', 'release_platform')
    template_name = 'console/test_case/test_case_update.html'

    # def get_success_url(self):
    #     release = Release.objects.get(pk=self.kwargs.get("pk"))
    #     return reverse('console:release_list', kwargs={'pk': release.project.id})


class TestCaseDeleteView(DeleteView):
    model = TestCase
    template_name = 'console/test_case/test_case_delete.html'
    #
    # def get_success_url(self):
    #     release = Release.objects.get(pk=self.kwargs.get("pk"))
    #     return reverse('console:test_case_list', kwargs={'pk': release.project.id})
