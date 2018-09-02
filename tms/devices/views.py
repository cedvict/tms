from django.urls import reverse_lazy
from django.views import generic
from .forms import DeviceForm
from .models import Device


from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class DeviceOverviewView(generic.DetailView):
    model = Device
    template_name = 'devices/device_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        return context


class DeviceCreateView(generic.CreateView):
    template_name = 'devices/create_device.html'
    form_class = DeviceForm
    success_url = reverse_lazy('dashboard')


class DeviceUpdateView(generic.UpdateView):
    model = Device
    template_name = 'devices/update_device.html'
    form_class = DeviceForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        return context


class DeviceReadView(generic.DetailView):
    model = Device
    template_name = 'devices/read_device.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['does_enter_a_device'] = True
    #     return context


class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = 'devices/device_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        device = Device.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        context['GLOBAL_PROJECT_ID'] = device.pk
        context['GLOBAL_PROJECT_NAME'] = device.name
        return context


class DeviceDeleteView(generic.DeleteView):
    model = Device
    template_name = 'devices/delete_device.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_project'] = False
        return context


class DeviceIndex(generic.ListView):
    model = Device
    context_object_name = 'devices'
    template_name = 'devices/device_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        devices = Device.objects.all()
        context['all_devices_list'] = devices
        context['does_enter_a_project'] = False
        return context
