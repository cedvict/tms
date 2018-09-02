# Django
from django.urls import path
# Local
from news import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('news/create/', views.NewsCreateView.as_view(), name='create_news'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='update_news'),
    path('news/<int:pk>/read', views.NewsReadView.as_view(), name='read_news'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete_news')
]
