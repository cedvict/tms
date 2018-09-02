# Django
from django.urls import path
# Local
from test_runs import views

app_name = 'test_runs'
urlpatterns = [
    path('test_run/', views.TestRunOverviewView.as_view(), name='test_run_overview'),
    path('test_run/create/', views.TestRunCreateView.as_view(), name='create_test_run'),
    path('test_run/<int:pk>/update', views.TestRunUpdateView.as_view(), name='update_test_run'),
    path('test_run/<int:pk>/read', views.TestRunReadView.as_view(), name='read_test_run'),
    path('test_run/<int:pk>/delete', views.TestRunDeleteView.as_view(), name='delete_test_run')
]
