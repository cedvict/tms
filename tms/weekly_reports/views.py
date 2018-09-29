from django.urls import reverse_lazy
from django.views import generic
from .forms import WeeklyReportForm
from .models import WeeklyReport


from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class WeeklyReportOverviewView(generic.DetailView):
    model = WeeklyReport
    template_name = 'weekly_reports/weekly_report_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        return context


class WeeklyReportCreateView(generic.CreateView):
    template_name = 'weekly_reports/create_weekly_report.html'
    form_class = WeeklyReportForm
    success_url = reverse_lazy('dashboard')


class WeeklyReportUpdateView(generic.UpdateView):
    model = WeeklyReport
    template_name = 'weekly_reports/update_weekly_report.html'
    form_class = WeeklyReportForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        return context


class WeeklyReportReadView(generic.DetailView):
    model = WeeklyReport
    context_object_name = 'weekly_report'
    template_name = 'weekly_reports/read_weekly_report.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_weekly_report'] = True
    #     return context


class WeeklyReportDetailView(generic.DetailView):
    model = WeeklyReport
    template_name = 'weekly_reports/weekly_report_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        weekly_report = WeeklyReport.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        context['GLOBAL_PROJECT_ID'] = weekly_report.pk
        context['GLOBAL_PROJECT_NAME'] = weekly_report.name
        return context


class WeeklyReportDeleteView(generic.DeleteView):
    model = WeeklyReport
    template_name = 'weekly_reports/delete_weekly_report.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        return context


class WeeklyReportIndex(generic.ListView):
    model = WeeklyReport
    context_object_name = 'weekly_reports'
    template_name = 'weekly_reports/weekly_report_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weekly_reports = WeeklyReport.objects.all()
        context['all_weekly_reports_list'] = weekly_reports
        context['does_enter_a_project'] = False
        return context
