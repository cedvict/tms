# Django
from django.urls import path
# Local
from test_runs import views

urlpatterns = [
    path('', views.Index.as_view(), name='dashboard'),
    path('test_run/', views.TestRunOverviewView.as_view(), name='test_run_overview'),
    path('test_run/create/', views.TestRunCreateView.as_view(), name='create_test_run'),
    path('test_run/update/<int:pk>', views.TestRunUpdateView.as_view(), name='update_test_run'),
    path('test_run/read/<int:pk>', views.TestRunReadView.as_view(), name='read_test_run'),
    path('test_run/delete/<int:pk>', views.TestRunDeleteView.as_view(), name='delete_test_run')
]
