from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import FormView, TemplateView

from console.forms import ContactFormSet, ContactForm, FilesForm
from console.views import fieldfile


class DefaultFormsetView(FormView):
    template_name = "console/example/formset.html"
    form_class = ContactFormSet


class DefaultFormView(FormView):
    template_name = "console/example/form.html"
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = "console/example/form_by_field.html"
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = "console/example/form_horizontal.html"
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = "console/example/form_inline.html"
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = "console/example/form_with_files.html"
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", "vertical")
        return context

    def get_initial(self):
        return {"file4": fieldfile}


class PaginationView(TemplateView):
    template_name = "console/example/pagination.html"

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
    template_name = "console/example/misc.html"
