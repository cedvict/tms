# Django
from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.Index.as_view(), name='dashboard'),
    path('my_work/', views.MyWorkView.as_view(), name='my_work'),
]
