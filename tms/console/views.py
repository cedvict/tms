# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views import generic
from django.db.models import Q

from django.contrib import messages

from .forms import ContactForm, FilesForm, ContactFormSet

from .models import Project, Message, Release, TestRun

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, "dummy.txt")


class HomePageView(TemplateView):
    template_name = "console/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['all_project_list'] = projects
        context['last_five_messages_list'] = Message.objects.all().order_by('-id')[:5]

        test_run_stats = {}
        for p in projects:
            test_run_stats[p.id] = TestRun.objects.filter(Q(project__id=p.id),
                                                        Q(test_run_status=TestRun.TEST_RUN_STATUS_CREATED) | Q(
                                                            test_run_status=TestRun.TEST_RUN_STATUS_ACTIVE) | Q(
                                                            test_run_status=TestRun.TEST_RUN_STATUS_BLOCKED)).count()
        context['test_run_stats'] = test_run_stats

        release_stats = {}
        for p in projects:
            release_stats[p.id] = Release.objects.filter(Q(project__id=p.id),
                                                        Q(release_status=Release.RELEASE_STATUS_CREATED) | Q(
                                                            release_status=Release.RELEASE_STATUS_ACTIVE)).count()
        context['release_stats'] = release_stats

        # messages.info(self.request, "hello http://example.com")
        return context


class DefaultFormsetView(FormView):
    template_name = "console/formset.html"
    form_class = ContactFormSet


class DefaultFormView(FormView):
    template_name = "console/form.html"
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = "console/form_by_field.html"
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = "console/form_horizontal.html"
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = "console/form_inline.html"
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = "console/form_with_files.html"
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", "vertical")
        return context

    def get_initial(self):
        return {"file4": fieldfile}


class PaginationView(TemplateView):
    template_name = "console/pagination.html"

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(200):
            lines.append("Line %s" % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get("page")
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context["lines"] = show_lines
        return context


class MiscView(TemplateView):
    template_name = "console/misc.html"


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'console/overview.html'


class TestRunView(generic.DetailView):
    model = Project
    template_name = 'console/test_run.html'


class TestCaseView(generic.DetailView):
    model = Project
    template_name = 'console/test_case.html'


class ReleaseView(generic.DetailView):
    model = Project
    template_name = 'console/release.html'
