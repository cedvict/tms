# Django
from django.urls import path
# Local
from news import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('news/create/', views.NewsCreateView.as_view(), name='create_news'),
    path('news/update/<int:pk>', views.NewsUpdateView.as_view(), name='update_news'),
    path('news/read/<int:pk>', views.NewsReadView.as_view(), name='read_news'),
    path('news/delete/<int:pk>', views.NewsDeleteView.as_view(), name='delete_news')
]
