# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Local
from .forms import NewsForm
from .models import News


class Index(generic.ListView):
    model = News
    context_object_name = 'News'
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_News'] = False
        return context


class NewsOverviewView(generic.ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_overview.html'


class NewsCreateView(generic.CreateView):
    template_name = 'news/create_news.html'
    form_class = NewsForm
    success_url = reverse_lazy('index')


class NewsUpdateView(generic.UpdateView):
    model = News
    template_name = 'news/update_news.html'
    form_class = NewsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['does_enter_a_news'] = True
        return context


class NewsReadView(generic.DetailView):
    model = News
    template_name = 'news/read_news.html'


class NewsDeleteView(generic.DeleteView):
    model = News
    template_name = 'news/delete_news.html'
    success_url = reverse_lazy('index')

