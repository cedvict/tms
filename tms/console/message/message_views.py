from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from console.models import Message


class MessageListView(generic.ListView):
    model = Message
    template_name = 'console/message/message_list.html'


class MessageCreateView(CreateView):
    model = Message
    template_name = 'console/message/message_add.html'
    # exclude = ('created_date', 'upd_date')
    fields = '__all__'

    def get_success_url(self):
        return reverse('console:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    exclude = ('created_date', 'upd_date')
    fields = '__all__'
    template_name = 'console/message/message_update.html'

    def get_success_url(self):
        return reverse('console:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'console/message/message_delete.html'

    def get_success_url(self):
        return reverse('console:message_list')

