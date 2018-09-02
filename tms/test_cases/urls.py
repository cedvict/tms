# Django
from django.urls import path
# Local
from test_cases import views

urlpatterns = [
    path('', views.Index.as_view(), name='dashboard'),
    path('test_case/', views.TestCaseOverviewView.as_view(), name='test_case_overview'),
    path('test_case/create/', views.TestCaseCreateView.as_view(), name='create_test_case'),
    path('test_case/<int:pk>/update', views.TestCaseUpdateView.as_view(), name='update_test_case'),
    path('test_case/<int:pk>/read', views.TestCaseReadView.as_view(), name='read_test_case'),
    path('test_case/<int:pk>/delete', views.TestCaseDeleteView.as_view(), name='delete_test_case')

]
