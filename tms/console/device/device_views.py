from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from console.models import Device


class DeviceListView(generic.ListView):
    model = Device
    template_name = 'console/device/device_list.html'


class DeviceCreateView(CreateView):
    model = Device
    template_name = 'console/device/device_add.html'
    # exclude = ('created_date', 'upd_date')
    fields = '__all__'

    def get_success_url(self):
        return reverse('console:device_list')


class DeviceUpdateView(UpdateView):
    model = Device
    exclude = ('created_date', 'upd_date')
    fields = '__all__'
    template_name = 'console/device/device_update.html'

    def get_success_url(self):
        return reverse('console:device_list')


class DeviceDeleteView(DeleteView):
    model = Device
    template_name = 'console/device/device_delete.html'
    success_url = reverse_lazy('console:device_list')
